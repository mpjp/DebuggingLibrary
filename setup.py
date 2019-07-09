import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mpjp-debuggingLibray",
    version="1.0.0",
    description="Library for remote chrome browser",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mpjp/DebuggingLibrary",
    author="mpjp",
    author_email="ingridchen82@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=["DebuggingLibrary"],
    include_package_data=True,
    install_requires=["robotframework-seleniumlibrary", "selenium"],
)