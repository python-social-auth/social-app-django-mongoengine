# -*- coding: utf-8 -*-
"""Setup file for easy installation"""
from os.path import join, dirname
from setuptools import setup


def long_description():
    return open(join(dirname(__file__), 'README.md')).read()

def load_requirements():
    lines = open(join(dirname(__file__), 'requirements.txt')).readlines()
    return [line for line in lines if not line.startswith('-e')]

def load_dependency_links():
    lines = open(join(dirname(__file__), 'requirements.txt')).readlines()
    return [line for line in lines if line.startswith('-e')]

setup(
    name='social-auth-app-django-mongoengine',
    version=__import__('social_django_mongoengine').__version__,
    author='Matias Aguirre',
    author_email='matiasaguirre@gmail.com',
    description='Python Social Authentication, Mongoengine Django integration.',
    license='BSD',
    keywords='django, social auth, mongoengine',
    url='https://github.com/python-social-auth/social-app-django-mongoengine',
    packages=[
        'social_django_mongoengine'
    ],
    long_description=long_description(),
    install_requires=load_requirements(),
    dependency_linkes=load_dependency_links(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Internet',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],
    zip_safe=False
)
