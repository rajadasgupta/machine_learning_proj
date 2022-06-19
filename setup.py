from setuptools import find_packages, setup
from typing import List

def get_requirements_list()->List[str]:
    """
    Description:
    return:
    """
    with open(REQUIREMENT_FILE_NAME)as requirement_file:
        return requirement_file.readlines().remove("-e .")


#Declaring variables for setup fucntions
PROJECT_NAME="Housing-Predictor"
VERSION="0.0.1"
AUTHOR="Raja Dasgupta"
DESCRIPTION="This is first machine learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(), #packages; find_packages automatically finds all packages
install_requires=get_requirements_list()
)