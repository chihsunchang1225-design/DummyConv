from setuptools import setup, find_packages

setup(
    name="dummyconv",
    version="0.1.0",  # 未來可以改成 0.2.0 來測試更新
    description="A test package for 3-layer CNN",
    packages=find_packages(),
    install_requires=["torch>=1.9.0"], 
)