import sys
from setuptools import setup

setup(
    name = "helloworld",        # what you want to call the archive/egg
    version = "0.1",
    packages=["helloworld"],    # top-level python modules you can import like
                                #   'import foo'
    dependency_links = [],      # custom links to a specific project
    install_requires=[],
    extras_require={},
    package_data = {},
    author="David Barnett",
    author_email = "davidbarnett2@gmail.com",
    description = "The familiar example program in Python",
    license = "BSD",
    keywords= "example documentation tutorial",
    url = "http://github.com/dbarnett/python-helloworld",
    entry_points = {
        "console_scripts": [
            "helloworld_in_python = helloworld.main:main",
        ]
    }
)