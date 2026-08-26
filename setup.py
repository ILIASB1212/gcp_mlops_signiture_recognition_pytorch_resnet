from setuptools import setup, find_packages

def get_requirements( ) :
    with open("requirements.txt", "r") as f:
        return f.read().splitlines()
    

setup(
    name="signiture recognition",
    version="1.0",
    author="ILIAS",
    packages=find_packages(),
    install_requires=get_requirements())

