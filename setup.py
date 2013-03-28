#!/usr/bin/env python
# encoding=utf-8

from setuptools import setup

entry_points = {
    'console_scripts': [
        'fasteignamat = fasteignamat:main',
    ]
}

setup(
    name='fasteignamat',
    version='0.1',
    url='https://github.com/pallih/fasteignamat-functions',
    license='UNLICENSE',
    author=u'Páll Hilmarsson',
    author_email='pallih@kaninka.net',
    description='Fetch info on landnr and fastanr from skra.is, the Icelandic real estate registry.',
    long_description=open('README.md').read(),
    py_modules=['fasteignamat'],
    zip_safe=False,
    include_package_data=True,
    install_requires=['requests', 'lxml'],
    entry_points=entry_points,
    platforms='any',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
