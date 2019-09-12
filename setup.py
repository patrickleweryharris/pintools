import re
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = re.search('^__version__ *= *"(.*)"',
                    open('pintools/pintools.py').read(), re.M).group(1)

setuptools.setup(
    name="pintools",
    version=version,
    author="Patrick Harris",
    author_email="patrick@plh.io",
    description="Tools importing links from various services to Pinboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patrickleweryharris/pintools",
    packages=["pintools"],
    entry_points={"console_scripts": ['pintools = pintools.pintools:main']},
    install_requires=["pinboard", "praw", "PyGithub"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires='>=3.5',
)
