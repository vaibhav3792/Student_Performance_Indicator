from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    with open(file_path) as file:
        requirements = file.readlines()
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.1.0',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
    author='Vaibhav Gupta',
    author_email= 'vaibhavgupta8807@gmail.com'
)