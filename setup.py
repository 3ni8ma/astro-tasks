from setuptools import setup, find_packages

setup(
    name="astro-tasks",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "astro=astro_tasks.cli:main",
        ],
    },
    install_requires=[
        "colorama>=0.4.6",
        "requests>=2.28.0",
    ],
    python_requires=">=3.8",
)
