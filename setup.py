import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="namebase-marketplace",
    version="0.0.7",
    python_requires='>=3.6',
    author="Roberto Pérez (pretended)",
    author_email="robertforperez@gmail.com",
    description="Python Client to interact with the Namebase Marketplace API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wy/namebase-exchange-python",
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
    ]
)