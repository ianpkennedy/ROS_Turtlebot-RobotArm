

from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

"""
This is the setup python file for the homework2 package
"""

a = generate_distutils_setup(packages = ['homework2'],package_dir={'':'src'})
setup(**a)

