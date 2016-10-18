#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pystreams',
    version='0.0.1',
    description="A framework to do stuff",
    long_description=readme,
    author="Kai und Max",
    author_email='kai.bruegge@tu-dortmund.de',
    url='https://github.com/mackaiver/pystreams',
    packages=[
        'pystreams',
    ],
    package_dir={'pystreams':
                 'pystreams'},
    entry_points={
        'console_scripts': [
            'pystreams=pystreams.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pystreams',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
