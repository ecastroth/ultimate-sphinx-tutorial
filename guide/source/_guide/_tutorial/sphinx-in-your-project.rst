=======================================
Adding and using Sphinx in your project
=======================================

Initializing Sphinx
===================

First of all, you'll need to initialize Sphinx in this project. For that, 
create a ``docs`` directory. Your dirtree must look like this:

.. code-block:: none
   :caption: Starting directory tree

   docs/
   src/
   ├── lib1/
   │   ├── file1.py
   │   ├── file2.py
   │   └── ...
   ├── lib2/
   │   ├── file1.py
   │   ├── file2.py
   │   └── ...
   ├── file.py
   └── ...
   main.py

Then initialize Sphinx inside the ``docs`` directory using:

.. code-block:: bash

   sphinx-quickstart

This command will ask you for:

#. ``> Separate source and build directories (y/n) [n]:`` y

#. ``> Project name:`` Normally the same as the git repo

#. ``> Author names(s):`` The authors of the code developed

#. ``> Project release []:`` Version name such as 1.0, Alpha, etc.

#. ``> Project language [en]:`` en

After this you'll have the following dirtree inside ``docs``:

.. code-block:: none
   :caption: Directory tree after Sphinx initialize
   
   docs/
   ├── build/
   └── source/
       ├── _static/
       ├── _templates/
       ├── conf.py
       └── index.rst
   Makefile
   make.bat

The ``source`` directory contains a collection of plain-text document sources 
and the configuration file ``conf.py``, where you can configure all aspects of 
how Sphinx reads your sources and builds your documentation.

The ``build`` directory contains the automatic generated documentation in the 
format that you specified in the ``conf.py`` file (for example html, LaTeX,
etc).

To make life easier, some Makefiles are also in the directory. These implement 
an standard way to building the documentation.


Building documentation
======================

You can build the documentation from the files in the ``source`` dir using:

.. code-block:: bash

   make html

If you want to further personalize your build, refer to the 
`sphinx-build <https://www.sphinx-doc.org/en/master/man/sphinx-build.html>`_
command documentation.

If you are following the steps, a ``html`` directory will appear inside your 
``build`` directory. The file that contains the (really ugly, by the way) 
landing page of your documentation is ``index.html`` and if you open it inside 
your web explorer you'll see that is empty.


Filling up the documentation
============================

The ``conf.py`` file
----------------------

To make your documentation look nice, work with different languages, use the 
docstrings that you write in the source code, change themes and customize them
and many more; you'll need to use a custom ``conf.py`` file like the following:

.. literalinclude:: ../../_static/conf.py
   :caption: conf.py
   :language: python
   :lineno-start: 1
   :emphasize-lines: 13-15, 34-36, 47-48, 51-75, 83, 91-

Where the lines that differ from the default ``conf.py`` file generated when 
initializing Sphinx are emphasized. 

Beside the default configuration accepted by this file, you can also make use
of 
`extensions <https://www.sphinx-doc.org/en/master/usage/extensions/index.html>`_
(either built-in or made by Third-parties). If you want to know what this 
configurations affect your docuementation, you can read the tangent on:

.. toctree::
   :maxdepth: 1

   config-deeper-look


Creating the ``.rst`` to the code files
---------------------------------------

.. warning:: This section is currently in development

So, you have made the effort to add docstings to your code and you've set up 
Sphinx to build the documentation, but now, how do you connect this things 
together?

To do this, Sphinx provides a command to automatically create the 
reStructuredText files from the documentation inside your code:

.. code-block:: bash

   sphinx-apidoc -o SOURCE_DIR DESTINATION_DIR

where ``DESTINATION_DIR`` is the directory where the generated ``.rst`` files 
from the ``SOURCE_DIR`` are going to be saved. Normally, you want the 
``DESTINATION_DIR`` to be something as ``docs/source/_MODULE_autodoc`` where 
``MODULE`` is the name of the module you're documenting.

For the case presented in this demo, you'll want to do (inside the ``docs`` 
dir):

.. code-block:: bash

   sphinx-apidoc -o source/_autodoc .. 
   sphinx-apidoc -o source/_autodoc ../src


Adding the files to ``index.rst``
---------------------------------

.. warning:: This section is currently in development