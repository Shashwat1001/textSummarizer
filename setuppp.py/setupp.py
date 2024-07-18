# setup.py
from setuptools import setup, find_packages

setup(
    name="textSummarizer",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'textsummarizer=textSummarizer.main:main',
        ],
    },
)
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
_version_ = "0.0.0"
REPO_NAME = "textSummarizer"
AUTHOR_USER_NAME = "reetika"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "rs4994@srmist.edu.in"

setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)