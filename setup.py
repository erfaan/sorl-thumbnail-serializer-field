import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='sorl-thumbnail-serializer-field',
    version='0.1',
    packages=['sorl_thumbnail_serializer'],
    include_package_data=True,
    license='MIT License',
    description='A sorl-thumbnail field for use with django-rest-framework.',
    long_description=README,
    url='https://github.com/dessibelle/sorl-thumbnail-serializer-field',
    author='Simon Fransson',
    author_email='simon@dessibelle.se',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'sorl-thumbnail',
        'djangorestframework',
    ],
)
