from setuptools import find_packages,setup
from typing import List

const = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [r.replace("\n","") for r in requirements]

        if const in requirements:
            requirements.remove(const)

    return requirements

setup(
    name = 'Data_transformation',
    version = '0.0.1',
    author = 'Madhumitha',
    author_email = 'ME20BTECH11022@iith.ac.in',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)