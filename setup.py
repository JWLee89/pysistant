"""
    @Author Jay Lee
    Pysistant setup file.
"""
from setuptools import setup

setup(name='Pysistant',
      version='0.0.1',
      description='A simple library of utility functions',
      url='https://github.com/JWLee89/pysistant',
      author='Jay Lee',
      author_email='ljay189@gmail.com',
      license='MIT',
      packages=['deeplearning', 'file', 'logging', 'matplotlib', 'os', 'util'],
      zip_safe=False)