import setuptools

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="namebase-marketplace",
    version="0.2.82",
    python_requires='>=3.6',
    author="Roberto Pérez Rico (pretended)",
    author_email="robertforperez@gmail.com",
    description="Python Client to interact with the Namebase Marketplace API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pretended/namebase-marketplace",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English'
    ],

)