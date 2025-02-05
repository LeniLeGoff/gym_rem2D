#!/usr/bin/env python
from setuptools import setup

setup(name='Modular_robtics_2D',
      description="Modular robotics 2D environment for OpenAi-Gym",
      version='0.1.0',
      keywords="modular robotics gym openai-gym",
      author="Frank Veenstra and Joergen Nordmoen",
      author_email="frankvee@uio.no",
      include_package_data=True,
      install_requires=['gym>=0.18', 'numpy>=1.17'],
      test_suite='tests',
      py_modules=["Encodings","gym_rem","gym_rem2D"])
