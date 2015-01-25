#-*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
with open(requirements_path, "r") as f:
    REQUIREMENTS = [x.strip() for x in f.readlines()]

REQUIREMENTS = REQUIREMENTS[1:]


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


EXCLUDE_FROM_PACKAGES = ['testapp']


setup(
    name='django-hbs-makemessages',
    version='0.9.1',
    license='MIT',
    description='Library providing makemessages for Handlebars.js templates',
    long_description=README,
    url='https://github.com/rafalp/django-hbs-makemessages',
    author=u'Rafał Pitoń',
    author_email='kontakt@rpiton.com',
    install_requires=REQUIREMENTS,
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    scripts=[
        'django-admin-hbs.py'
    ],
    test_suite="test.main",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
