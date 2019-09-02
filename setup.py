import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pintools",
    version="0.0.1",
    author="Patrick Harris",
    author_email="patrick@plh.io",
    description="Tools importing links from various services to Pinboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patrickleweryharris/pintools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires='>=3.5',
)
