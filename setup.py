from setuptools import setup, find_packages
from os import path

__version__ = '0.0.4'

here = path.abspath(path.dirname(__file__))

# Get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = [
        x.strip()
        for x in f.read().splitlines()
        if x.strip() and not x.startswith('#')
    ]

install_requires = [x for x in all_reqs if not x.startswith('git+')]
dependency_links = [x.replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='mlfromscratch',
    version=__version__,
    description=(
        'Python implementations of some of the fundamental Machine Learning '
        'models and algorithms from scratch.'
    ),
    url='https://github.com/eriklindernoren/ML-From-Scratch',
    download_url='https://github.com/eriklindernoren/ML-From-Scratch/tarball/master',
    license='MIT',
    packages=find_packages(exclude=['.venv', 'tests', 'tests.*']),
    include_package_data=True,
    author='Erik Linder-Noren',
    author_email='eriklindernoren@gmail.com',
    install_requires=install_requires + ['numpy>=1.10', 'scipy>=0.17'],
    dependency_links=dependency_links,
    python_requires='>=3.7',
)
