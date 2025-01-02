"""
Setup file for the meteodata package
"""

from setuptools import setup, find_packages

# read the requirements.txt file
with open("requirements.txt", "r") as file:
    requirements = file.read().splitlines()

setup(
    name="download_mf_tools",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,
)
