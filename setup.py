import os
from setuptools import setup, find_packages


def read(*paths):
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', "-"))
    ]


setup(
    name="dundies",
    version="0.1.1",
    description="Reward points system for Dunder Mifflin",
    author="Mader",
    python_requires=">=3.10",
    packages=find_packages(exclude=["integration"]),
    include_package_data=True,
    entry_points={"console_scripts": ["dundie = dundie.__main__:main"]},
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "test": read_requirements("requirements.test.txt"),
        "dev": read_requirements("requirements.dev.txt"),
    },
)
