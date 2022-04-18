from setuptools import setup, find_packages
from pathlib import Path


VERSION = '0.0.18'
DESCRIPTION = 'Linear Algebra Calculator with simple functions'
#LONG_DESCRIPTION = 'A linear algebra function that uses python to calculate values such as the inverse or transpose of a matrix and much more'
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="linearAlgebraCalc",
    version=VERSION,
    author="Aditya Srikanth",
    author_email="aditya.srikanth11@gmail.com" ,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description, 
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'mathamatics', 'Linear Algebra', 'Vectors', 'Eigen Values'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

'''
python3 setup.py bdist_wheel  
twine upload --skip-existing dist/*
'''