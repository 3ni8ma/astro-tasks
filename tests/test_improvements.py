"""RED tests for astro-tasks improvements.

Covers: unread-count helper, git_status on real repos,
threaded data collection, and user config file loading.
"""
import json
import os
import subprocess
import threading
from unittest.mock import patch

from astro_tasks import cli
from astro_tasks import config
from astro_tasks import github_check
from astro_tasks import repo_check


# --- 1. Unread-count helper ---------------------------------------------

def test_count_unread_mixed_notifications():
    notifs = [
        {"unread": True},
        {"unread": False},
        {"unread": True},
        {},  # missing key counts as read
    ]
    assert github_check.count_unread(notifs) == 2


def test_count_unread_empty():
    assert github_check.count_unread([]) == 0


# --- 2. git_status on real repos -----------------------------------------

def _make_repo(path, dirty=False):
    os.makedirs(path, exist_ok=True)
    subprocess.run(["git", "init", "-q"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.email", "t@t.t"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=path, check=True)
    with open(os.path.join(path, "f.txt"), "w") as f:
        f.write("hi")
    subprocess.run(["git", "add", "."], cwd=path, check=True)
    subprocess.run(["git", "commit", "-qm", "init"], cwd=path, check=True)
    if dirty:
        with open(os.path.join(path, "f.txt"), "a") as f:
            f.write("more")


def test_git_status_clean_repo(tmp_path):
    d = str(tmp_path / "clean")
    _make_repo(d)
    branch, info, err = repo_check.git_status(d)
    assert err is None
    assert branch
    assert info["dirty"] is False
    assert info["unpushed"] == -1  # no remote configured


def test_git_status_dirty_repo(tmp_path):
    d = str(tmp_path / "dirty")
    _make_repo(d, dirty=True)
    branch, info, err = repo_check.git_status(d)
    assert err is None
    assert info["dirty"] is True


def test_git_status_unpushed_with_remote(tmp_path):
    origin = str(tmp_path / "origin.git")
    subprocess.run(["git", "init", "-q", "--bare", origin], check=True)
    d = str(tmp_path / "work")
    subprocess.run(["git", "clone", "-q", origin, d], check=True)
    subprocess.run(["git", "config", "user.email", "t@t.t"], cwd=d, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=d, check=True)
    with open(os.path.join(d, "f.txt"), "w") as f:
        f.write("hi")
    subprocess.run(["git", "add", "."], cwd=d, check=True)
    subprocess.run(["git", "commit", "-qm", "one"], cwd=d, check=True)
    branch, info, err = repo_check.git_status(d)
    assert err is None
    # origin/<branch> doesn't exist yet -> reported as no remote tracking
    assert info["unpushed"] == -1


def test_git_status_not_a_repo(tmp_path):
    branch, info, err = repo_check.git_status(str(tmp_path))
    assert branch is None and info is None
    assert err == "not a git repo"


# --- 3. Threaded collection ----------------------------------------------

def test_collect_check_data_runs_fetchers_concurrently():
    barrier = threading.Barrier(3)
    seen_threads = []
    lock = threading.Lock()

    def make_getter(payload):
        def _get():
            barrier.wait(timeout=10)
            with lock:
                seen_threads.append(threading.get_ident())
            return payload, None
        return _get

    with patch("astro_tasks.cli.github_check.get_notifications",
               side_effect=make_getter([{"unread": True}])), \
         patch("astro_tasks.cli.github_check.get_open_prs",
               side_effect=make_getter([])), \
         patch("astro_tasks.cli.wakatime_check.get_stats",
               side_effect=make_getter({})), \
         patch("astro_tasks.cli.repo_check.git_status",
               return_value=("main", {"unpushed": 0, "dirty": False}, None)):
        data = cli.collect_check_data()

    assert len(set(seen_threads)) == 3  # each fetcher on its own thread
    assert data["github"]["unread_notifications"] == 1


# --- 5. WakaTime default API endpoint ---------------------------------------

def test_wakatime_defaults_to_official_api_url(tmp_path, monkeypatch):
    from astro_tasks import wakatime_check
    cfg = tmp_path / "wakatime.cfg"
    cfg.write_text("[settings]\napi_key = fakekey\n")
    monkeypatch.setattr(config, "WAKATIME_CFG", str(cfg))

    captured = {}

    class FakeResp:
        def __enter__(self): return self
        def __exit__(self, *a): return False
        def read(self): return b'{"data": {}}'

    def fake_urlopen(req, timeout=10):
        captured["url"] = req.full_url
        return FakeResp()

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    data, err = wakatime_check.get_stats()
    assert err is None
    assert captured["url"].startswith("https://wakatime.com/api/v1/")
    assert data == {}

# --- 4. User config file --------------------------------------------------

def test_load_user_config_from_file(tmp_path, monkeypatch):
    cfg_file = tmp_path / "config.json"
    cfg_file.write_text(json.dumps({
        "github_user": "someone",
        "machine_name": "My-Mac",
        "repos": [{"name": "demo", "dir": "/tmp/demo"}],
    }))
    monkeypatch.setattr(config, "CONFIG_PATH", str(cfg_file))
    assert config.get_github_user() == "someone"
    assert config.get_machine_name() == "My-Mac"
    assert config.get_repos() == [{"name": "demo", "dir": "/tmp/demo"}]


def test_env_overrides_config_file(tmp_path, monkeypatch):
    cfg_file = tmp_path / "config.json"
    cfg_file.write_text(json.dumps({"github_user": "file-user"}))
    monkeypatch.setattr(config, "CONFIG_PATH", str(cfg_file))
    monkeypatch.setenv("ASTRO_GITHUB_USER", "env-user")
    assert config.get_github_user() == "env-user"


def test_missing_config_file_falls_back_to_defaults(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "CONFIG_PATH", str(tmp_path / "none.json"))
    monkeypatch.delenv("ASTRO_GITHUB_USER", raising=False)
    assert config.get_github_user() == "3ni8ma"
    assert isinstance(config.get_repos(), list)
