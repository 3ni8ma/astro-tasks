from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="astro-tasks",
    version="0.1.2",
    description="Pre-flight checklist for developers — GitHub status, coding stats, repo health in one command",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/3ni8ma/astro-tasks",
    author="Aarush Karak",
    license="MIT",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "astro=astro_tasks.cli:main",
        ],
    },
    install_requires=[
        "colorama>=0.4.6",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
