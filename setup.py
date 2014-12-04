# encoding: utf-8
from setuptools import setup, find_packages
from frigga_snake import version

setup(
    name = 'frigga-snake',
    version = version,
    description = 'Netflix\' Frigga in Python',
    author = u'Kristian Øllegaard',
    author_email = 'kristian@plecto.com',
    zip_safe=False,
    include_package_data = True,
    packages = find_packages(exclude=[]),
    install_requires=[
        'nose'
    ],
)