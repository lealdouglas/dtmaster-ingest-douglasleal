from setuptools import setup, find_packages

setup(
    name="dtmasteringestdougsll",
    version="0.0.1",
    author="Douglas Leal",
    author_email="douglas.sleal@outlook.com",
    description="An application test for ingest",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["dtmasteringestdougsll = src.main:main"]},
)