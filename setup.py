from setuptools import find_packages, setup # setuptools is used for packaging Python projects
from typing import List

HYPEEN_E_DOT = '-e.'

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    :param file_path: Path to the requirements file
    :return: List of requirements
    """
    requirements = []
    # Open the requirements file and read its contents
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]  # Remove newline characters
        
    if HYPEEN_E_DOT in requirements:
        requirements.remove(HYPEEN_E_DOT)  # Remove editable install requirement if present
    return requirements

setup(
    name='Fault detection',
    version='0.0.1',
    author='RNoSin',
    author_email='rnosin@example.com',
    install_requirements=get_requirements('requirements.txt',),
    packages=find_packages(),
    description='A package for fault detection in industrial systems'
)