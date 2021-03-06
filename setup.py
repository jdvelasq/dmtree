from setuptools import setup, find_packages

#
# How to install:
#
#    python3 setup.py sdist
#    twine upload dist/*
#

setup(
    name="smart_choice",
    version="0.0.0",
    author="Juan D. Velasquez",
    author_email="jdvelasq@unal.edu.co",
    license="MIT",
    url="http://github.com/jdvelasq/smart-choice",
    description="Decision Making Analysis",
    long_description="Decision Analysis using Decision Trees for Prescriptive Analytics",
    keywords="analytics",
    platforms="any",
    provides=["smart_choice"],
    install_requires=[
        "numpy",
        "matplotlib",
        "graphviz",
    ],
    packages=find_packages(),
    package_dir={"smart_choice": "smart_choice"},
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
