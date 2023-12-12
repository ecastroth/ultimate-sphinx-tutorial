==========================
Code development guideline
==========================

This page contains the styling guideline for writting Python code. This 
standard is based on the `PEP8 <https://peps.python.org/pep-0008>`_,
`PEP257 <https://peps.python.org/pep-0257/>`_,
`PEP483 <https://peps.python.org/pep-0483/>`_,
`PEP484 <https://peps.python.org/pep-0484/>`_,
`PEP526 <https://peps.python.org/pep-0526/>`_ and
`PEP604 <https://peps.python.org/pep-0604/>`_ guidelines.

Code Layout
===========

Indentation
-----------
The code written must use **4 spaces per indentation**. Continuation lines 
should align wrapped elements either vertically or using hanging indent, as 
shown in the example below.

.. code-block:: python

   # Vertically aligned with opening delimiter
   foo = long_function_name(var_one, var_two,
                            var_three, var_four)                          
   
   # Hanging indent
   # In functions, add an extra level of indentation to distinguish args
   def long_function_name(
           var_one, var_two, var_three,
           var_four):
       pass
   
   # When calling a callable, hanging indents should add a level
   foo = long_function_name(
       var_one, var_two,
       var_three, var_four)


When the conditional part of an ``if``-statement requires more than one line, 
the conditional statement should be written as follows.

.. code-block:: python

   if (this_one_thing
       and this_is_another_thing):
       do_something()

      
The closing brace/bracket/parenthesis on multiline constructs must line up 
under the first non-whitespace character of the last line of list, as in:

.. code-block:: python

   # List
   my_list = [
       1, 2, 3,
       4, 5, 6
       ]

   # Callable
   result = some_function_that_takes_arguments(
       'a', 'b', 'c',
       'd', 'e', 'f',
       )


Use of Tabs and Spaces
----------------------
You must **always** use spaces instead of tabs.


Maximum line lenght
-------------------
The line lenght must be limited to:

*  For coments and docstrings: 75 characters is mandatory and cannot be 
   agreeded by the developing team.
*  For code: 79 characters is the default accepted lenght. Nevertheless the
   size can be set up to a 99 characters by the developing team.

The preferred way of wrapping long lines is by braking lines into multiple 
lines of expressions wrapped up by parentheses (using backslash for line 
continuation).

.. code-block:: python

   with open('/path/to/some/file/you/want/to/read') as file_1, \
        open('/path/to/some/file/being/written', 'w') as file_2:
       file_2.write(file_1.read())


Should a line break before or after a binary operator?
------------------------------------------------------
Python uses the mathematicians convention:

.. code-block:: python

   income = (gross_wages
             + taxable_interest
             + (dividends - qualified_dividends)
             - ira_deduction
             - student_loan_interest)

Blank lines
-----------
Surround using:

*  **1 blank line:** Method definitions inside a class. 
*  **2 blank lines:** Top-level function and class definitions with two blank 
   lines.

Use blank lines in functions, sparingly, to indicate logical sections.


Source file encoding
--------------------
Code should always use **UTF-8** and should not have an encoding declaration. 
Non-ASCII characters can be used only to denote places and human names. If 
using non-ASCII characters as data, avoid noisy Unicode chars as z̯̯͡a̧͎̺l̡͓̫g̹̲o̡̼̘.

Code must be use the English language.


Imports
-------
Imports should allways be on **separated lines** and at the **top of the 
file**, before module globals and constants, and **should be grouped** in the 
following order:

#. Standard library imports
#. Related third party imports
#. Local application/library specific imports

With the groups separated by one blank line.

.. code-block:: python

   import os
   import csv

   import numpy as np
   import pandas as pd

   from . import example
   from mypkg import example


String quotes
=============
Even though for Python ``'`` and ``"``  are the same, we'll use ``'`` for 
string quotes on code.

When a string contains ``'`` or ``"``, however, use the other one to avoid the 
use of ``\`` in the string.

Triple-quoted strings always use double quote characters to be consistent with 
`PEP257 <https://peps.python.org/pep-0257/>`_.


Whitespace in expresions and statements
=======================================

Pet peeves
----------
Avoid extraneous whitespace in the following situations:

*  Immediately inside parentheses, brackets or braces:

   .. code-block:: python

      # Correct:
      spam(ham[1], {eggs: 2})


*  Between a trailing comma and a following close parenthesis:

   .. code-block:: python
      
      # Correct:
      foo = (0,)


*  Immediately before a comma, semicolon, or colon:

   .. code-block:: python

      # Correct:
      if x == 4: print(x, y); x, y = y, x


*  However, in a slice the colon acts like a binary operator, and should have 
   equal amounts on either side. In an extended slice, both colons must have 
   the same amount of spacing applied. 
   
   **Exception:** when a slice parameter is omitted, the space is omitted:

   .. code-block:: python

      # Correct:
      ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
      ham[lower:upper], ham[lower:upper:], ham[lower::step]
      ham[lower+offset : upper+offset]
      ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
      ham[lower + offset : upper + offset]

      # Wrong:
      ham[lower + offset:upper + offset]
      ham[1: 9], ham[1 :9], ham[1:9 :3]
      ham[lower : : step]
      ham[ : upper]

      
*  More than one space around an assignment (or other) operator to align it 
   with another:

   .. code-block:: python
      
      # Correct:
      x = 1
      y = 2
      long_variable = 3

      # Wrong:
      x             = 1
      y             = 2
      long_variable = 3


Other recommendations
---------------------
*  Always surround these binary operators with a single space on either side: 
   assignment (``=``), augmented assignment (``+=``, ``-=``, etc.), comparisons 
   (``==``, ``<``, ``>``, ``!=``, ``<>``, ``<=``, ``>=``, ``in``, ``not in``, 
   ``is``, ``is not``), Booleans (``and``, ``or``, ``not``). If operators with 
   different priorities are used, consider adding whitespace around the 
   operators with the lowest priority(ies).

   .. code-block:: python
      
      # Correct:
      i = i + 1
      submitted += 1
      x = x*2 - 1
      hypot2 = x*x + y*y
      c = (a+b) * (a-b)

*  Function annotations should allways use spaces around the ``->`` arrow.

*  Don't use spaces around the ``=`` sign when used to indicate a keyword 
   argument, or when used to indicate a default value for an *unannotated* 
   function parameter:

   .. code-block:: python

      # Correct:
      def complex(real, imag=0.0):
          return magic(r=real, i=imag)


Comments
========
Comments should be complete sentences. The first word should be capitalized, 
unless it is an identifier that begins with a lower case letter (never alter 
the case of identifiers!) and be written in English.

**Comments that contradict the code are worse than no comments.**


Block comments
--------------
Block comments generally apply to some (or all) code that follows them, and are
indented to the same level as that code. Each line of a block comment starts 
with a ``#`` and a single space (unless it is indented text inside the comment).

Paragraphs inside a block comment are separated by a line containing a single 
``#``.


Naming conventions
==================

Descriptive: Naming styles
--------------------------
Some important style convention names are:
*  ``CapitalizeWords`` (also known as CapWords or CamelCase).
*  ``mixedCase`` (differs from CapWords by initial lowercase char).
*  ``lower_case_with_underscores``.

.. note::
   When using acronyms in CapWords, capitalize all the letters of the acronym 
   e.g. ``HTTPServerError`` is better than ``HttpServerError``.


The following special forms using leading or trailing undescores are accepted:

*  ``_single_leading_underscore``: weak “internal use” indicator.
*  ``single_trailing_underscore_``: used by convention to avoid conflicts with 
   Python keywords.
*  ``__double_leading_and_trailing_underscore__``: “magic” objects or 
   attributes. Never invent such names; only use them as documented.


Prescriptive: Naming Conventions
--------------------------------
*  Never use ``l``, ``O`` or ``I`` as single character variable names.
*  Modules should have short, all-lowercase names. 
*  Class names should use the CapWords convention.
*  Exceptions should be classes and use the suffix “Error” (if the exception is actually is an error).
*  Global variables are meant for use inside one module only. Modules with them
   should use the ``__all__`` mechanism to prevent exporting globals.
*  Functions, Methods and Global names should be mixedCase.
*  Variable names should be lowercase, with words separated by underscores as 
   necessary to improve readability.
*  Non-public methods should use one leading underscore.
*  Constants should be defined on a module level and written in all caps with 
   underscores separating words.
*  Allways decide whether a class's methods and attributes should be public or
   non-public. If in doubt choose non-public. (Read 
   `Designing for Inheritance <https://peps.python.org/pep-0008/#designing-for-inheritance>`_).

Public and Internal Interfaces
------------------------------
Any backwards compatibility guarantees apply only to public interfaces. 
Accordingly, it is important that users be able to clearly distinguish between 
public and internal interfaces.

To better support introspection, modules should explicitly declare the names in 
their public API using the ``__all__`` attribute. Setting ``__all__`` to an 
empty list indicates that the module has no public API.


Programming recommendations
===========================
*  Comparisons to singletons like ``None`` should always be done with ``is`` or 
   ``is not``, never the equality operators.


*  Use ``is not`` operator rather than ``not ... is``.


*  Always use a ``def`` statement instead of an assignment statement that binds
   a lambda expression directly to an identifier:

   .. code-block:: python

      # Correct:
      def f(x): return 2*x

      # Wrong:
      f = lambda x: 2*x


   The first form means that the name of the resulting function object is 
   specifically '``f``' instead of the generic '``<lambda>``'.


*  Derive exceptions from ``Exception`` rather than ``BaseException``.


*  Use exception chaining appropriately. ``raise X from Y`` should be used to 
   indicate explicit replacement without losing the original traceback.


*  When catching exceptions, mention specific exceptions whenever possible 
   instead of using a bare ``except:`` clause. A good rule of thumb is to limit
   use of bare '``except``' clauses to two cases:

   a. If the exception handler will be printing out or logging the traceback.
   b. If the code needs to do some cleanup work, but then lets the exception 
      propagate upwards with ``raise``.


*  For all ``try`` / ``except`` clauses, limit the ``try`` clause to the 
   absolute minimum amount of code necessary. Again, this avoids masking bugs: 

   .. code-block:: python

      # Correct:
      try:
          value = collection[key]
      except KeyError:
          return key_not_found(key)
      else:
          return handle_value(value)
      
      # Wrong:
      try:
          # Too broad!
          return handle_value(collection[key])
      except KeyError:
          # Will also catch KeyError raised by handle_value()
          return key_not_found(key)


*  Either all ``return`` statements in a function should return an expression, 
   or none of them should. An explicit return statement should be present at 
   the end of the function (if reachable):

   .. code-block:: python

      # Correct:
      def foo(x):
          if x >= 0:
              return math.sqrt(x)
          else:
              return None

      # Correct:
      def bar(x):
          if x < 0:
              return None
          return math.sqrt(x)

      # Wrong:
      def foo(x):
          if x >= 0:
              return math.sqrt(x)

      # Wrong:
      def bar(x):
          if x < 0:
              return
          return math.sqrt(x)


*  Use ``''.startswith()`` and ``''.endswith()`` instead of string slicing to 
   check for prefixes or suffixes.

   .. code-block:: python

      # Correct:
      if foo.startswith('bar'):

      # Wrong:
      if foo[:3] == 'bar':


*  Object type comparisons should always use ``isinstance()`` instead of
   comparing types directly:

   .. code-block:: python

      # Correct:
      if isinstance(obj, int):

      # Wrong:
      if type(obj) is type(1):

   
*  For sequences (strings, lists, tuples) use the fact that empty sequences are
   ``False``:

   .. code-block:: python

      # Correct:
      if not seq:
      if seq:

      # Wrong:
      if len(seq):
      if not len(seq):


*  Don't compare boolean values to ``True`` or ``False`` using ``==``:

   .. code-block:: python

      # Correct:
      if greeting:

      # Wrong:
      if greeting == True:

      # Worse:
      if greeting is True:


*  Use of the flow control statements ``return`` / ``break`` / ``continue`` 
   within the finally suite of a ``try...finally``, where the flow control 
   statement would jump outside the ``finally`` suite, is discouraged.

   .. code-block:: python

      # Wrong:
      def foo():
          try:
              1 / 0
          finally:
              return 42


Type Hints
==========
While the proposal is accompanied by an extension of the 
``typing.get_type_hints`` standard library function for runtime retrieval of 
annotations, variable annotations are not designed for runtime type checking. 
Third party packages are developed to implement such functionality.

It should also be emphasized that **Python will remain a dynamically typed 
language, and the authors have no desire to ever make type hints mandatory, 
even by convention**. Type annotations should not be confused with variable 
declarations in statically typed languages. The goal of annotation syntax is to
provide an easy way to specify structured type metadata for third party tools.

Gradual typing and the full type system are explained in `The theory of Type 
Hints (PEP483) <https://peps.python.org/pep-0483/>`_.


General annotations
-------------------
In its basic form, type hinting is used by filling function annotation slots 
with classes:

.. code-block:: python

   def greeting(name: str) -> str:
       return 'Hello ' + name

This states that the expected type of the ``name`` argument is ``str``. 
Analogically, the expected return type is ``str``.

Acceptable type hints
^^^^^^^^^^^^^^^^^^^^^
Type hints may be built-in classes (including those defined in standard library
or third-party extension modules), abstract base classes, types available in 
the ``types module``, and user-defined classes (including those defined in the 
standard library or third-party modules). 

In addition to the above, the following special constructs defined below may be
used: ``None``, ``Any``, ``Union``, ``Tuple``, ``Callable``, all ``ABC``s and 
stand-ins for concrete classes exported from ``typing`` (e.g. ``Sequence`` and 
``Dict``), type variables, and type aliases.

A resume of the ``typing`` module can be found on 
`PEP484 - The Typing module <https://peps.python.org/pep-0484/#the-typing-module>`_.


Type aliases
^^^^^^^^^^^^
Type aliases are defined by simple variable assignments:

.. code-block:: python

   Url = str

   def retry(url: Url, retry_count: int) -> None: ...


Note that is recommended capitalizing alias names, since they represent 
user-defined types, which (like user-defined classes) are typically spelled 
that way.

Type aliases may be as complex as type hints in annotations and anything that 
is acceptable as a type hint is acceptable in a type alias:

.. code-block:: python

   from typing import TypeVar, Iterable, Tuple

   T = TypeVar('T', int, float, complex)
   Vector = Iterable[Tuple[T, T]]

   def inproduct(v: Vector[T]) -> T:
      return sum(x*y for x, y in v)
   def dilate(v: Vector[T], scale: T) -> Vector[T]:
      return ((x * scale, y * scale) for x, y in v)
   vec = []  # type: Vector[float]


TypeVar
^^^^^^^
A ``TypeVar()`` expression must always directly be assigned to a variable (it 
should not be used as part of a larger expression). The argument to 
``TypeVar()`` must be a string equal to the variable name to which it is 
assigned. Type variables must not be redefined.

``TypeVar`` supports constraining parametric types to a fixed set of possible 
types (Note that those types cannot be parameterized by type variables). 
For example, we can define a type variable that ranges over just ``str`` and 
``bytes``. By default, a type variable ranges over all possible types. 
Example of constraining a type variable:

.. code-block:: python

   from typing import TypeVar, Text

   AnyStr = TypeVar('AnyStr', Text, bytes)

   def concat(x: AnyStr, y: AnyStr) -> AnyStr:
       return x + y

The function ``concat`` can be called with either two ``str`` arguments or two 
``bytes`` arguments, but not with a mix of ``str`` and ``bytes`` arguments.

Special types
^^^^^^^^^^^^^
Some of the special types include:

*  **The** ``Union`` **type**
   Since accepting a small, limited set of expected types for a single argument
   is common, there is a new special factory called ``Union``. A type factored 
   by ``Union[T1, T2, ...]`` is a supertype of all types ``T1``, ``T2``, etc., 
   so that a value that is a member of one of these types is acceptable for an 
   argument annotated by ``Union[T1, T2, ...]``.

   One common case of union types are optional types. By default, ``None`` is 
   an invalid value for any type, unless a default value of ``None`` has been 
   provided in the function definition. For example:

   .. code-block:: python
      
      def handle_employee(e: Union[Employee, None] = None) -> None: ...


   As a shorthand for ``Union[T1, None]`` you can write ``Optional[T1]``; 
   for example, the above is equivalent to:

   .. code-block:: python
      
      from typing import Optional

      def handle_employee(e: Optional[Employee] = None) -> None: ...
   
   Also, since `PEP604 <https://peps.python.org/pep-0604/>`_ you can hint a 
   ``Union`` of types using the ``|`` operator. For example:

   .. code-block:: python

      int | str == typing.Union[int, str]
      None | t == typing.Optional[t]

   If you want to use this syntaxis I'll recommend you marry to use either 
   ``Union`` or the ``|`` operator but not both for consistency.


*  **The** ``Any`` **type**
   Every type is consistent with ``Any``. It can be considered a type that has 
   all values and all methods. Besides this, Any is the assumed type for 
   function parameter without an annotation and generic types without 
   specifying type parameters.   


*  **The** ``NoReturn`` **type**
   The ``typing`` module provides a special type ``NoReturn`` to annotate 
   functions that never return normally. For example, a function that 
   unconditionally raises an exception:

   .. code-block:: python

      from typing import NoReturn

      def stop() -> NoReturn:
         raise RuntimeError('no way')
   

   The ``NoReturn`` type is only valid as a return annotation of functions, and 
   considered an error if it appears in other positions.


Exceptions
^^^^^^^^^^
No syntax for listing explicitly raised exceptions is proposed. Currently the 
only known use case for this feature is documentational, in which case the 
recommendation is to put this information in a docstring.


Variable annotations
--------------------
`PEP484 <https://peps.python.org/pep-0484/>`_ introduced type hints, a.k.a. 
type annotations. While its main focus was function annotations, it also 
introduced the notion of type comments to annotate variables. Although type 
comments work well enough, the fact that they're expressed through comments has
some downsides that are be alleviated by the 
`PEP526 <https://peps.python.org/pep-0526/>`_. A resume of this PEP is given in 
the following example:

.. code-block:: python

   # Correct:
   code: int

   class Point:
       coords: Tuple[int, int]
       label: str = '<unknown>' 

   # Wrong:
   code:int  # No space after colon
   code : int  # Space before colon

   class Test:
       result: int=0  # No spaces around equality sign

I recommend to use variable annotations only on variables that must be set by 
the user and have not any default value inside the script.


Function annotations
--------------------
Any function without annotations will be treated as having the most general 
type possible, or ignored, by any type checker. Functions with the 
``@no_tyep_check decorator`` should be treated as having no annotations. For a 
checked function, the default annotation for arguments and for the return type 
is ``Any``.

It's recommended that all functions have some form of type hinting.