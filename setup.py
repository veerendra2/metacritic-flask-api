#!/usr/bin/python3
import sys
import setuptools
from setuptools.command.install import install

version = sys.version_info[:2]
if (3, 0) < version < (3, 4):
    print('metacritic_api requires Python version 3.4 or later ({}.{} detected).'.format(*version))
    sys.exit(1)

setuptools.setup(
    name='metacritic_api',
    version='0.1',
    description='metacritic API',
    author='Veerendra Kakumanu',
    packages=setuptools.find_packages(where="src"),
    install_requires=["beautifulsoup4", "waitress", "Flask", "requests"],
    entry_points={'console_scripts': [
        'metacritic_api = metacritic_api:main']},
    package_dir={'': 'src'},
    python_requires=">=3.4",
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "Development Status :: 4 - Beta"
    ],
    zip_safe=False)
