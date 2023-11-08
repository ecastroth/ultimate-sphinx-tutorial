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
===========================

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

.. literalinclude:: ../_static/conf.py
   :caption: conf.py
   :language: python
   :lineno-start: 1
   :emphasize-lines: 13-15, 34-36, 47-48, 51-75, 83, 91-
   :name: conf.py

Where the lines that differ from the default ``conf.py`` file generated when 
initializing Sphinx are emphasized. As you can see, the ``conf.py`` file is a
Python file that is known as the *"build configuration file"* and contains *on 
most cases* all the configuration needed to customize Sphinx input and output
behavior.

Beside the default configuration accepted by this file, you can also make use
of 
`extensions <https://www.sphinx-doc.org/en/master/usage/extensions/index.html>`_
(either built-in or made by Third-parties). This will be discussed on the 
sections ahead.


Built-in modifications
^^^^^^^^^^^^^^^^^^^^^^

First of all, you'll need to say to Sphinx where the directory with your code 
is, relative to the :ref:`conf.py` file. This is done on the lines:

.. literalinclude:: ../_static/conf.py
   :caption: conf.py lines 13 to 15
   :language: python
   :start-at: import os
   :end-at: sys.path.insert
   :lineno-start: 13

The line 47 adds the Sphinx default texts language for the project:

.. literalinclude:: ../_static/conf.py
   :caption: conf.py lines 47 and 48
   :language: python
   :start-at: # Language
   :end-at: language
   :lineno-start: 47

Line 83 sets the theme of the documentation to be the 
`PyData Sphinx Theme <https://pydata-sphinx-theme.readthedocs.io/en/>`_. The 
same one used by 
`NumPy <https://numpy.org/doc/stable/>`_, 
`Jupyter <https://docs.jupyter.org/en/latest/>`_, 
`Matplotlib <https://matplotlib.org/stable/>`_, 
`Pandas <https://pandas.pydata.org/docs/>`_, 
`SciPy <https://docs.scipy.org/doc/scipy/>`_ 
and many other great projects *-so even if your project is not that great, I 
asure you that your documentation will be-*.

.. literalinclude:: ../_static/conf.py
   :caption: conf.py line 83
   :language: python
   :start-at: html_theme
   :end-at: html_theme
   :lineno-start: 83


Customizing the theme
^^^^^^^^^^^^^^^^^^^^^

As you can see, the :ref:`conf.py` file ads a section for theme customization. 
You can find a full description of the configuration posibilities on the 
`User Guide <https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/index.html>`_.

The configuration regarding the configuration of the theme founded on the 
:ref:`conf.py` contains two main sections. The lines 93 to 96 configures the 
**left sidebar**,

.. literalinclude:: ../_static/conf.py
   :caption: conf.py lines 93 to 96
   :language: python
   :start-at: # Sidebar configuration
   :end-at: }
   :lineno-start: 93

This code adds two items:

#. A search bar.
#. A bootstrap-friendly navigation section. When there are no pages to show, it
   dissapears.

On the other hand, lines 98 to 112 adds some **little tweaks**:

.. literalinclude:: ../_static/conf.py
   :caption: conf.py lines 98 to 112
   :language: python
   :start-at: # General theme options
   :lineno-start: 98

* Line 101 sets the title of the documentation (on the left upper corner). In 
  this guide, the text logo is "The ultimate Sphinx tutorial".
* Line 103 adds the light/black theme color switch and a icon bar with links to
  the upper navigation bar.
* Lines 105 to 112 configure the icons to display on the upper right corner, as
  you can see, a GitHub icon is added with a link to the repository of this 
  guide


Extensions
^^^^^^^^^^
As it was discussed, Sphinx make use of extensions to add some functionalities 
to your documentation, such as automatic use of docstrings, autosummary of 
objects in files or syntaxis detection of syle (such as NumpyDocs). Some of 
this extensions come **built-in** with Sphinx and others are developed by
**third-parties**, which can be installed using ``pip``.

Here, we'll cover the extensions used on the :ref:`conf.py` file. As you can 
see the extensions used are listed on the lines 33 to 37:

.. literalinclude:: ../_static/conf.py
   :caption: conf.py lines 33 to 37
   :language: python
   :start-at: extensions = [
   :end-at: ]
   :lineno-start: 34
   :name: extension-list

Extensions allow for custom/further configuration, in the :ref:`conf.py` file, 
it can be found on the section from line 51 to 75:

.. literalinclude:: ../_static/conf.py
   :caption: conf.py lines 51 to 75
   :language: python
   :start-at: # -- Extension config
   :end-at: myst_heading_anchors
   :lineno-start: 51
   :name: extension-config


**Built-in extensions**

A rule of thumb to catch which extensions are built-in with sphinx, is that its
names allways begin with ``sphinx.ext.NAME``, where ``NAME`` is the name of the
extension. On the config file, 3 built-in extensions are activated:

1. ``sphinx.ext.viewcode`` *(explicitly, as is in the list)*

   This extension allow for the ``Show Source`` button to appear on the right 
   sidebar. This extension does not have any extra configuration on the 
   :ref:`extension-config`.

2. ``sphinx.ext.autosummary`` *(implicitly, by the use of* ``numpydoc`` *)*

   This extension generates function/method/attribute summary lists and its 
   especially useful when your docstrings are long and detailed, and putting 
   each one of them on a separate page makes them easier to read.

   The configuration of this extension can be found on lines 70 to 72 on 
   :ref:`extension-config`:

   * ``autosummary_generate``: create `.rst` with a table with the objects 
     inside files summarized. The file can be generated passing a custom 
     template.
   * ``autosummary_generate_overwrite``: create new `.rst` on every build.

   You can find further information of this extension on the 
   `autosummary documentation page <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_.

3. ``sphinx.ext.autodoc`` *(implicitly, by the use of* ``numpydoc`` *)*

   This extension import the modules you are documenting, and pull in 
   documentation from docstrings in a automatic way.

   The configuration of this extension can be found on lines 58 to 68 on
   :ref:`extension-config`:

   *  ``autodoc_default_options``:

      The default options for autodoc directives. They are applied to all 
      autodoc directives automatically. 

      ``members``: 
         autodoc will generate document for the members of the target module,
         class or exception (recursively)

      ``undoc-members``:
         autodoc will not generate document for the members not having 
         docstings

      ``private-members``: 
         autodoc will also generate document for the private members

   * ``autodoc_typehints``: 
     No typehints are shown.

   You can find further information of this extension on the 
   `autodoc documentation page <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_.

A full list of Sphinx built-in extensions and links to its documentations can 
be found 
`here <https://www.sphinx-doc.org/en/master/usage/extensions/index.html#built-in-extensions>`_.


**Thrid-parties extensions**

Only two third party extensions are used on the config file:

1. ``numpydoc``:
   This extension provides support for the Numpy docstring format in Sphinx.

   The configuration of this extension can be found on lines 53 to 56 on 
   :ref:`extension-config`:

   * ``numpydoc_show_class_members``:
     Show all members of a class in the Methods and Attributes sections 
     automatically.
   * ``numpydoc_class_members_toctree``
     Do not create a Sphinx table of contents for the lists of class methods 
     and attributes.
   * ``numpydoc_show_inherited_class_members``
     Do not show all inherited members of a class in the Methods and Attributes
     sections automatically.

   You can find more information about this extension in the 
   `NumpyDocs documentation <https://numpydoc.readthedocs.io/en/latest/index.html>`_.


2. ``myst-parser``:
   Translate Markdown files to reStructuredText files, allowing the use of 
   `.md` files into the documentation. 
   An example of this can be found on the use of the file 
   `How to write DocStrings <docstrings-guidelines.html>`_. Possibly you
   didn't even notice, but if you see the source code you'll see its a Markdown
   file!

   The only configuration on the :ref:`extension-config` regarding this 
   extension is found on line 75. ``myst_heading_anchors`` is used only for 
   Markdown header references inside file, such as 
   ``[link to header](#SOME-HEADER)`` to work.

   You can find more information about this extension in the 
   `MyST Parser documentation <https://myst-parser.readthedocs.io/en/latest/index.html>`_.


Creating the ``.rst`` files
---------------------------

So, you have made the effort to add docstings to your code and you've set up 
Sphinx to build the documentation, but now, how do you connect this things 
together?

To do this, Sphinx provides a command to automatically create the re-Structured
Text files from the documentation inside your code:

.. code-block:: bash

   sphinx-apidoc -o SOURCE_DIR DESTINATION_DIR

where ``DESTINATION_DIR`` is the directory where the generated ``.rst`` files 
with the documentation of the ``SOURCE_DIR`` are going to be saved. Normally, 
you want the ``DESTINATION_DIR`` to be something as 
``docs/source/_MODULE_autodoc`` where ``MODULE`` is the name of the module 
you're documenting.

For the case presented in this demo, you'll want to do (inside the ``docs`` 
dir):

.. code-block:: bash

   sphinx-apidoc -o source/_autodoc .. 
   sphinx-apidoc -o source/_autodoc ../src


Adding the files to ``index.rst``
---------------------------------

.. warning:: This section is currently in development


Further customization
=====================