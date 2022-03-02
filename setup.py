try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
  name = 'pymonte',
  packages = ['pymonte'],
  version = '1.0.0',
  description = 'A lightweight Python library for running simple Monte Carlo experiments.',
  author = 'Ahmed Aly',
  author_email = 'ahmedzak.23@gmail.com',
  url = 'https://github.com/zachdotai/monte-carlo-simulator',
  download_url = 'https://github.com/zachdotai/monte-carlo-simulator/archive/master.zip',
)
