#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

install_requires = [
    'Click>=6.0',
]

tests_require = [
    'pytest>=3.0.0'
]

setup_requires = [
    'pytest'
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
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
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
)
