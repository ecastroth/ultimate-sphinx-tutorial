=======================================
Adding and using Sphinx in your project
=======================================

This page contains a step-by-step tutorial on how to add Sphinx to your project
in a basic way. Also, I include:

*  :doc:`Taking your documentation to the next level <to-the-next-level>`: The 
   section you need to see after this to take your documentation a step up 
   through the power of extensions.
*  :doc:`A further look on the conf.py file <conf-deeper-look>`: An optional 
   tangent on how the ``conf.py`` file works and some of the tweaks used for 
   this tutorial.


.. toctree::
   :hidden:

   to-the-next-level
   conf-deeper-look


Initializing Sphinx
===================

First of all, you'll need to initialize Sphinx in this project. For that, 
create a ``docs`` directory. Your dirtree must look like this:

.. code-block:: none
   :caption: Starting directory tree

   component/
   ├── package1/
   │   ├── subpackage2/
   │   │   ├── __init__.py
   │   │   ├── subfile1.py
   │   │   └── subfile2.py
   │   ├── subpackage2/
   │   │   ├── __init__.py
   │   │   ├── subfile1.py
   │   │   └── subfile2.py
   │   ├── __init__.py
   │   ├── file1.py
   │   └── file2.py
   ├── __init__.py
   └── file1.py
   docs/
   guide/
   requirements/
   .gitignore
   README.md

Then initialize Sphinx inside the ``docs`` directory using:

.. code-block:: bash

   sphinx-quickstart

This command will ask you for:

#. ``> Separate source and build directories (y/n) [n]:`` y

#. ``> Project name:`` Normally the same as the git repo (for example Demorepo)

#. ``> Author names(s):`` The authors of the code developed

#. ``> Project release []:`` Version name such as 1.0, Alpha, etc.

#. ``> Project language [en]:`` en

After this you'll have the following dirtree inside ``docs``:

.. code-block:: none
   :caption: Directory tree after Sphinx initialize
   
   docs/
   ├── build/
   ├── source/
   │   ├── _static/
   │   ├── _templates/
   │   ├── conf.py
   │   └── index.rst
   │   Makefile
   └── make.bat

The ``source`` directory contains a collection of plain-text document sources 
and the configuration file ``conf.py``, where you can configure all aspects of 
how Sphinx reads your sources and builds your documentation.

The ``build`` directory contains the automatic generated documentation in the 
format that you specified in the ``conf.py`` file (for example html, LaTeX,
etc).

To make life easier, some Makefiles are also in the directory. These implement 
an standard way to building the documentation. You can further personalize the
commands that build your documentation using the
`sphinx-build <https://www.sphinx-doc.org/en/master/man/sphinx-build.html>`_ 
command.


Building documentation
======================

You can build the documentation from the files in the ``source`` dir using:

.. code-block:: bash

   make clean html

If you want to further personalize your build, refer to the 
`sphinx-build <https://www.sphinx-doc.org/en/master/man/sphinx-build.html>`_
command documentation.

.. warning:: The ``make clean`` part of the command is used to forcefully 
   remove the files from the ``build`` directory, forcing the documentation to 
   generate from from scratch (in this case in ``html`` format). This will be 
   useful on the sections ahead as we modify the files that generate the 
   documentation.

If you are following the steps, a ``html`` directory will appear inside your 
``build`` directory. The directory that contains the *-really ugly, by the 
way-* landing page of your documentation (``index.html``) and if you open it 
inside your web browser you'll see that is empty.


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
(either built-in in Sphinx or made by Third-parties). If you want to know how 
this lines affect your docuementation, you can read the tangent on: 
:doc:`A deeper look into the conf.py file <conf-deeper-look>`.


Translating code files to ``.rst`` files
----------------------------------------

So, you have made the effort to add docstings to your code and you've set up 
Sphinx to build the documentation, but now, how do you connect this things 
together?

To do this, Sphinx needs to have some files linking to your code. For this 
purpose, it provides a command to automatically create the reStructuredText 
files for every file in your code:

.. code-block:: bash

   sphinx-apidoc -o SOURCE_DIR DESTINATION_DIR -f

where ``DESTINATION_DIR`` is the directory where the generated ``.rst`` files 
from the ``SOURCE_DIR`` are going to be saved. Normally, you want the 
``DESTINATION_DIR`` to be something as ``docs/source/_MODULE_autodoc`` where 
``MODULE`` is the name of the module you're documenting (this is only to have 
some order). The ``-f`` flag forces that the previous generated files to be 
overwritten

.. note:: This command works recursively but only with packages i.e. modules inside 
   a directory with a ``__init__.py`` file created.

For the case presented in this demo, you'll want to do (inside the ``docs`` 
dir):

.. code-block:: bash

   sphinx-apidoc -o source/_component_autodoc ../component -f

You'll notice that a ``_component_autodoc`` dir has appeared inside the 
``source`` directory. 

.. code-block:: none
   :caption: Directory tree after Sphinx ApiDoc
   
   docs/
   ├── build/
   └── source/
      ├── _component_autodoc/
      │   ├── component.package1.rst
      │   ├── component.package1.subpackage1.rst
      │   ├── component.package1.subpackage2.rst
      │   ├── component.rst
      │   └── modules.rst
      ├── _static/
      ├── _templates/
      ├── conf.py
      └── index.rst

If you open the generated files, you'll see that they are standard ``.rst`` 
files that can be modified without problem. You can add text to them aswell as 
any other element supported by reStructuredText.

As you can see all the code has been detected because of the ``__init__.py`` 
files, you can try to delete them and see what changes. Also a ``modules.rst`` 
file has appeared with links to the different files in the root "component" 
directory.


Adding the files to ``index.rst``
---------------------------------

Now you'll have ``.rst`` files linking to your source code files, but if you 
build the documentation again nothing has change. For this, you'll need to add 
the files created to your ``index.rst`` file.

The ``index.rst`` file serves as a landing page for your documentation and it 
must contain *(at least)* a table of contents (TOC) of the main sections of 
your documentation. Lets use this as our ``index.rst`` file:

.. literalinclude:: ../../_static/basic-index.rst
   :caption: index.rst
   :language: rst
   :lineno-start: 1
   :emphasize-lines: 9-10, 12-16

As you can see, some text was added to this file. If you see the highlighted 
lines you'll see we added a table of contents tree (TOCtree) of depth 4 of the
``modules.rst`` file created automatically with the ``sphinx-apidoc`` command.

If you build your documentation now, you'll see finally its taking form. Feel 
free to navigate the current documentation and see the automatically generated 
source files to understand what is going on, as this will change a lot in the
next pages.