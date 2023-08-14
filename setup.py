from setuptools import setup
import sys,os

setup(
    name = 'testapp',
    version = '0.1.0',
    description = 'Python test package',
    license='GPL v3',
    author = 'my name',
    packages = ['src'],
    package_data={'src': ['description.txt']
                 },
    install_requires=['future'],
    entry_points = {
        'console_scripts': [
            'hello=src.app:main']
            },
    classifiers = ['Operating System :: OS Independent']
)