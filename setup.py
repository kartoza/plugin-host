import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='kartoza-plugins',
<<<<<<< HEAD
    version='0.2',
=======
    version='0.3',
>>>>>>> cffe4870b5fd61fd1ca6424a108a4a6a3c2f3b0d
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to host qgis plugins.',
    long_description=README,
    url='https://www.kartoza.com',
    author='Dimas Ciputra',
    author_email='dimas@kartoza.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
