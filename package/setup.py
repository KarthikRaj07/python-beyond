from setuptools import setup

from setuptools import setup, find_packages

setup(
    name="mypackage",           # Name of your package
    version="0.1",              # Version number
    packages=find_packages(),   # Automatically include sub-packages
    description="A sample Python package",  # Short description
    author="Karthik Raj K",         # Author name
    author_email="999karthikraj@gmail.com",  # Author email
    license="MIT",              # License type
    python_requires='>=3.6',    # Minimum Python version required


  zip_safe = False)