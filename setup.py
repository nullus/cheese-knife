import os
import setuptools

from cheese_knife import __version__

basedir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(basedir, "README.rst"), "r") as readme:
    __long_description__ = readme.read()

setuptools.setup(
    name='cheese_knife',
    version=__version__,
    packages=setuptools.find_packages(exclude=("test",)),
    url='https://github.com/nullus/cheese-knife',
    license='BSD',
    author='Dylan Perry',
    author_email='dylan.perry@gmail.com',
    description='Description goes here!',
    long_description=__long_description__,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Games/Entertainment',
    ],
    test_suite='test',
    install_requires=[
        'Flask',
    ],
    extras_require={
        'dev': [
            'Sphinx',
        ],
    },
)
