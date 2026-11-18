from setuptools import setup, find_packages

setup(
    name="dummyconv",
    version="0.1.1",
    description="A test package for 3-layer CNN",
    packages=find_packages(),
    install_requires=["torch>=1.9.0"], 
)