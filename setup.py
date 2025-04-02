from setuptools import find_packages,setup

def get_requirements(file_path):
    requirements = []
    with open('requirements.txt') as file:
        requirements=file.readlines()
        requirements = [req.replace('\n','')for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
    name='Energy Consumption',
    version='0.0.1',
    author='Tejas Kothavale',
    author_email='kothavaleptejas@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)