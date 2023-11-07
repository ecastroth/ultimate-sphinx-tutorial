"""This file uses the resources founded on the libraries 1 and 2.

This file its still inside the src directory"""

import src.lib1.file1 as l1f1
import src.lib2.file1 as l2f1
import src.lib1.file2 as l1f2
import src.lib2.file2 as l2f2

def someFunctionThatUsesThePackages():
    """Some docstrgins for a function that uses the elements of the lib1 and 
    lib2 packages"""
    a = l1f1.SomeClass()
    b = l2f1.SomeClass()
    c = l1f2.someFuntion()
    d = l2f2.someFuntion()
    return a, b, c, d