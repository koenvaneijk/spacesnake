import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding='utf-8')

setup(
    name="spacesnake",
    version="0.1.0",
    author="Koen van Eijk",
    author_email="vaneijk.koen@gmail.com",
    description="Python decentralized on IFPS",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        'click==7.1.2',
        'requests==2.25.1'
    ],
    entry_points={
        'console_scripts': [
            'spacesnake = spacesnake:cli'
        ]
    },
    license_files = ('LICENSE',)
)
