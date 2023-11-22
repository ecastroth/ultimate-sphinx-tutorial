"""This file uses the resources founded on the package 1.

This file could be the main file, or some other file from the repository"""

from .package1 import file1 as p1f1
from .package1 import file2 as p1f2

def someFunctionThatUsesThePackages():
    """Some docstrgins for a function that uses the elements of the lib1 and 
    lib2 packages"""
    p1f1.someFunction(1, 2)
    p1f2.someFunction1()
    p1f2.SomeClass1().someMethod1()
    print('Correct!')

if __name__ == '__main__':
    someFunctionThatUsesThePackages()