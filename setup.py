#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
]

setup_requirements = [
]

test_requirements = [
    'pytest',
]

setup(
    name='ohol',
    version='0.1.0',
    description=".",
    long_description=readme + '\n\n' + history,
    author="Florian Ludwig",
    author_email='f.ludwig@greyrook.com',
    url='https://github.com/FlorianLudwig/ohol',
    packages=find_packages(include=['ohol']),
    entry_points={
        'console_scripts': [
            'ohol=ohol.client_cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='ohol',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
