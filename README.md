# Linear Algebra Calculator

# About the Project
Throughout my sophmore year of college, myself and my engineering friends had a tough time with the Linear Algebra class, including various questions with matrix reduction, and solution finding. This python package aims to assist in some of the simple functions that needed to be computed in order to succeed in the linear algebra class. The package incldues functions ranging from simple four function operations to finding the solution of equations or determinent or transpose of a matrix etc... 

The package can be found with more information, and the source code on the website: https://pypi.org/project/linearAlgebraCalc/

## How to use
Upon installing and having python3 running on the local machine, running the command 

```bash
pip install linearAlgebraCalc
```
Version History: most recent up to date version is 1.21

After importing the package, in a python3 project the import statement 

```bash
import linearAlgebraCalc 
```

Using the functions presented by calling them as such ```bash linearAlgebraCalc.add() ```

Currently, the supported functions are listed in the following file directory: ```bash linearAlgebraCalc/__init__.py ```
Each individual function in that file is a working function that can be used in your program with the correct parameters. If incorrect parameters or incorrect fields are entered, appropriate error messages will return to console, allowing the user to understand their issue. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Requirments
1. sys
2. os
3. traceback
