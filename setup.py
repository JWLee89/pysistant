"""
    @Author Jay Lee
    Pysistant setup file.
"""
import setuptools


with open("README.md", 'r') as readme:
      long_description = readme.read()


setuptools.setup(
      name='Pysistant',
      version='0.0.1',
      description='A simple library of utility functions',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/JWLee89/pysistant',
      packages=setuptools.find_packages(),
      classifiers=[
           "Programming Language :: Python :: 3",
           "License :: OSI Approved :: MIT License",
           "Operating System :: OS Independent",
      ],
      author='Jay Lee',
      author_email='ljay189@gmail.com',
      license='MIT',
      python_requires='>=3.5',
      zip_safe=False)