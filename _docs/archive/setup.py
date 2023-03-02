# Note used until we define as a package, here as an example.
from setuptools import setup, find_packages

setup(
    name='mysharedmodule',
    version='1.0.0',
    description='A simple Python Module',
    author='Steve Robinson',
    author_email='steve@cloudy.dog',
    #packages=find_packages(),
    packages=[
    'mysharedmodule'
],
    #install_requires=[
    #    # Add any dependencies that your module requires
    #    'requests',
    #    'numpy',
    #],
)