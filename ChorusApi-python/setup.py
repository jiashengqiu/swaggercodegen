import sys
from setuptools import setup, find_packages



# To install the library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed.
# Try reading the setuptools documentation:
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi"]

setup(
    name="ChorusApi",
    version="v1",
    description="Chorus API",
    author_email="",
    url="",
    keywords=["Swagger", "Chorus API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The first version of the Chorus API is an exciting step forward towards\nmaking it easier for users to have open access to their data. We created it\nso that you can surface the amazing content chorus users share every\nsecond, in fun and innovative ways.\n\nBuild something great!\n
    """
)










