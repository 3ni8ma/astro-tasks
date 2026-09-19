"""RED test: astro check --json must return real check data, not a stub."""
from unittest.mock import patch

from astro_tasks import cli


def test_collect_check_data_returns_real_sections():
    with patch("astro_tasks.cli.github_check.get_notifications", return_value=([{"unread": True}], None)), \
         patch("astro_tasks.cli.github_check.get_open_prs", return_value=([{"number": 1, "title": "t", "headRefName": "a", "baseRefName": "b"}], None)), \
         patch("astro_tasks.cli.wakatime_check.get_stats", return_value=({"human_readable_total": "1 hr", "projects": [], "languages": []}, None)), \
         patch("astro_tasks.cli.repo_check.git_status", return_value=("main", {"unpushed": 0, "dirty": False}, None)):
        data = cli.collect_check_data()

    assert "github" in data
    assert "coding_stats" in data
    assert "repos" in data
    assert data["github"]["unread_notifications"] == 1
    assert data["github"]["open_prs_count"] == 1
    assert len(data["github"]["open_prs"]) == 1
