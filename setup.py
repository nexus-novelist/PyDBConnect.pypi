from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A private database service library.'
LONG_DESCRIPTION = 'A package that allows you to build your own database service on your home server!'

# Setting up
setup(
    name="pydbconnect",
    version=VERSION,
    author="NexusNovelist",
    author_email="<proffesionalnoice@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'database', 'server'],
    classifiers=[
        "Development Status :: 2 - Development",
        "Intended Audience :: Developers & IT",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)