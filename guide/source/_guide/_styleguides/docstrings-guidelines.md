# How to write DocStrings
Some of this file is based on the [PEP 257](https://peps.python.org/pep-0257/) standard, that PEP aims to standarize the high-level structure of docstrings: what they should contain, and how to say it (without touching on any markup syntax within docstrings).

The main resource for the development of this standard can be found is the [Sphinx documentation](https://www.sphinx-doc.org/en/master/) and the [NumpyDocs](https://numpydoc.readthedocs.io/en/latest/index.html) style standard.

All the code documentation for the project aims to be generated automatically using Sphinx vía the use of docstrings and plain text files written on [re-Structured Text (reST)](http://docutils.sourceforge.net/rst.html) or [Markdown](https://www.markdownguide.org/) markdown languaje with NumpyDocs as the style standard.


## What is a Docstring?
A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the `__doc__` special attribute of that object.

All modules should normally have docstrings, and all functions and classes exported by a module should also have docstrings. Public methods should also have docstrings. A package may be documented in the module docstring of the `__init__.py` file in the package directory.

For consistency, always use `"""triple double quotes"""` around docstrings:

```python
"""This is the form of a docstring.

It can be spread over several lines.

"""
```

The predominant docstring standard uses reST syntax and is rendered using [Sphinx](https://www.sphinx-doc.org/) (a pre-processor that understands the particular documentation style we are using). While a rich set of markup is available, we limit ourselves to a very basic subset, in order to provide docstrings that are easy to read on text-only terminals.

The length of docstring lines should be kept to 75 characters to facilitate reading the docstrings in text terminals.


## What is Sphinx?
Sphinx is a documentation generator or a tool that translates a set of plain text source files into various output formats, automatically producing cross-references, indices, etc. That is, if you have a directory containing a bunch of [re-StructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html) or [Markdown](https://www.sphinx-doc.org/en/master/usage/markdown.html) documents, Sphinx can generate a series of HTML files, a PDF file (via LaTeX), man pages and much more.


## Documentation style guides
As it was allready been stablished, the documentation *(and this tutorial)* will follow the [NumpyDocs style guides](https://numpydoc.readthedocs.io/en/latest/format.html).


### Documenting functions
The docstring consists of a number of sections separated by headings (except for the deprecation warning). Each heading should be underlined in hyphens, and the section ordering should be consistent with the description below.

A full list of the sections from a function docstrings can be found [here](https://numpydoc.readthedocs.io/en/latest/format.html#sections). Some of the most used are:

#### 1. Short summary
A one-line summary that does not use variable names or the function name, e.g.

```python
def add(a, b):
   """The sum of two numbers.

   """
```

#### 2. Extended summary
A few sentences giving an extended description. This section should be used to clarify functionality, not to discuss implementation detail or background theory, which should rather be explored in the [Notes](#9-notes) section below. You may refer to the parameters and the function name, but parameter descriptions still belong in the [Parameters](#3-parameters) section.

#### 3. Parameters
Description of the function arguments, keywords and their respective types.

```rst
Parameters
----------
x : type
    Description of parameter `x`.
y
    Description of parameter `y` (with type not specified).
```

Enclose variables in single backticks. The colon must be preceded by a space, or omitted if the type is absent.

For the parameter types, be as precise as possible.

If it is not necessary to specify a keyword argument, use `optional`:

```python
x : int, optional
```

Optional keyword parameters have default values, which are displayed as part of the type, instead of `optional`. If the default value would not be used as a value, `optional` is preferred. These are all equivalent:

```python
copy : bool, default True
copy : bool, default=True
copy : bool, default: True
```

When a parameter can only assume one of a fixed set of values, those values can be listed in braces, with the default appearing first:

```rst
order : {'C', 'F', 'A'}
    Description of `order`.
```

When two or more input parameters have exactly the same type, shape and description, they can be combined:

```rst
x1, x2 : array_like
    Input arrays, description of `x1`, `x2`.
```

#### 4. Returns
Explanation of the returned values and their types. Similar to the [Parameters](#3-parameters) section, except the name of each return value is optional. The type of each return value is always required:

```rst
Returns
-------
int
    Description of anonymous integer return value.
```

If both the name and type are specified, this section takes the same form as the [Parameters](#3-parameters) section:

```rst
Returns
-------
err_code : int
    Non-zero value indicates error code, or zero on success.
err_msg : str or None
    Human readable error message, or None on success.
```

#### 5. Yields
Explanation of the yielded values and their types. This is relevant to generators only. Must be written as [Returns](#4-returns).

#### 6. Raises
An optional section detailing which errors get raised and under what conditions:

```rst
Raises
------
LinAlgException
    If the matrix is not numerically invertible.
```

This section should be used judiciously, i.e., only for errors that are non-obvious or have a large chance of getting raised.

#### 7. Warnings
An optional section with cautions to the user in free text/reST.

#### 8. See Also
An optional section used to refer to related code. This section can be very useful, but should be used judiciously. The goal is to direct users to other functions they may not be aware of, or have easy means of discovering (by looking at the module docstring, for example). Routines whose docstrings further explain parameters used by this function are good candidates.

#### 9. Notes
An optional section that provides additional information about the code, possibly including a discussion of the algorithm. This section may include mathematical equations, written in [LaTeX](https://www.latex-project.org/) format:

```rst
Notes
-----
The FFT is a fast implementation of the discrete Fourier transform:

.. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}
```

Math can also be used inline. Note that LaTeX is not particularly easy to read, so use equations sparingly.

Images are allowed, but should not be central to the explanation; users viewing the docstring as text must be able to comprehend its meaning without resorting to an image viewer.

#### 10. References
References cited in the [Notes](#9-notes) section may be listed here, e.g. if you cited the article below using the text `[1]_`, include it as in the list as follows:

```rst
.. [1] O. McNoleg, "The integration of GIS, remote sensing,
   expert systems and adaptive co-kriging for environmental habitat
   modelling of the Highland Haggis using object-oriented, fuzzy-logic
   and neural-network techniques," Computers & Geosciences, vol. 22,
   pp. 585-588, 1996.
```

Referencing sources of a temporary nature, like web pages, is discouraged. References are meant to augment the docstring, but should not be required to understand it. References are numbered, starting from one, in the order in which they are cited.


### Documenting classes
#### Constructor docstrings
Use the same sections as outlined above (all except [Returns](#4-returns) are applicable). The constructor (`__init__`) should also be documented here, the [Parameters](#3-parameters) section of the docstring details the constructor’s parameters.

**Attributes**
An **Attributes** section, located below the [Parameters](#3-parameters) section, may be used to describe non-method attributes of the class:

```rst
Attributes
----------
x : float
    The X coordinate.
y : float
    The Y coordinate.
```

**Methods**
In general, it is not necessary to list class methods. Those that are not part of the public API have names that start with an underscore. In some cases, however, a class may have a great many methods, of which only a few are relevant (e.g., subclasses of ndarray). Then, it becomes useful to have an additional **Methods** section:

```python
class Photo(ndarray):
    """
    Array with associated photographic information.

    ...

    Attributes
    ----------
    exposure : float
        Exposure in seconds.

    Methods
    -------
    colorspace(c='rgb')
        Represent the photo in the given colorspace.
    gamma(n=1.0)
        Change the photo's gamma exposure.

    """
```

If it is necessary to explain a private method (use with care!), it can be referred to in the [Extended Summary](#2-extended-summary) or the [Notes](#9-notes) section. Do not list private methods in the **Methods** section.

Note that `self` is **not** listed as the first parameter of methods.

#### Methods docstrings
Document these as you would any other function. Do not include `self` in the list of parameters. If a method has an equivalent function (which is the case for many ndarray methods for example), the function docstring should contain the detailed documentation, and the method docstring should refer to it. Only put the [Brief summary](#1-short-summary) and [See Also](#8-see-also) sections in the method docstring. The method should use a [Returns](#4-returns) or [Yields](#5-yields) section, as appropriate.


### Documenting generators
Generators should be documented just as functions are documented. The only difference is that one should use the [Yields](#5-yields) section instead of the [Returns](#4-returns) section.


### Documenting constants
Use the same sections as outlined for functions where applicable:

1. summary
2. extended summary (optional)
3. see also (optional)
4. references (optional)
5. examples (optional)

Docstrings for constants will not be visible in text terminals (constants are of immutable type, so docstrings can not be assigned to them like for for class instances), but will appear in the documentation built with Sphinx.


### Documenting modules
Each module should have a docstring with at least a summary line. Other sections are optional, and should be used in the same order as for documenting functions when they are appropriate:

1. summary
2. extended summary
3. routine listings
4. see also
5. notes
6. references
7. examples

Routine listings are encouraged, especially for large modules, for which it is hard to get a good overview of all functionality provided by looking at the source file(s) or the `__all__` dict.

Note that license and author info, while often included in source files, do not belong in docstrings.


### Other points to keep in mind
#### Links
If you need to include hyperlinks in your docstring, note that some docstring sections are not parsed as standard reST. To avoid this problem use the inline hyperlink form:

```rst
`Example <http://www.example.com>`_
```

#### Notes and Warnings
If there are points in the docstring that deserve special emphasis, the reST directives for a note or warning can be used in the vicinity of the context of the warning (inside a section). Syntax:

```rst
.. warning:: Warning text.

.. note:: Note text.
```

Use these sparingly, as they do not look very good in text terminals and are not often necessary. One situation in which a warning can be useful is for marking a known bug that is not yet fixed.

#### Equations
As discussed in the [Notes](#9-notes) section above, LaTeX formatting should be kept to a minimum. Often it’s possible to show equations as Python code or pseudo-code instead, which is much more readable in a terminal. For inline display use double backticks, like:

    ``y = np.sin(x)``

For display with blank lines above and below, use a double colon and indent the code, like:

```rst
end of previous sentence::

    y = np.sin(x)
```

#### reST concepts
For paragraphs, indentation is significant and indicates indentation in the output. New paragraphs are marked with a blank line.

Use `*italics*`, `**bold**` and `monospace` if needed in any explanations (but not for variable names and doctest code or multi-line code). Variable, module, function, and class names should be written between single back-ticks (`numpy`).

Line spacing and indentation are significant and should be carefully followed.

A more extensive example of reST markup can be found in [this example document](http://docutils.sourceforge.net/docs/user/rst/demo.txt); the [quick reference](http://docutils.sourceforge.net/docs/user/rst/quickref.html) and [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) are useful while editing.