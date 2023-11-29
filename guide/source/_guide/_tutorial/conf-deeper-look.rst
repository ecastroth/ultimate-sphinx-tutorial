===============================
Deeper look on the conf.py file
===============================

So, the custom file we recommend in 
:doc:`Adding and using Sphinx in your project <sphinx-in-your-project>`
is:

.. literalinclude:: ../../_static/conf.py
   :caption: conf.py
   :language: python
   :lineno-start: 1
   :emphasize-lines: 13-15, 34-37, 48-49, 52-76, 84, 92-
   :name: conf.py

As you can see, the ``conf.py`` file is a Python file that is known as the 
*"build configuration file"* and contains *on most cases* all the configuration
needed to customize Sphinx input and output behavior.


Built-in modifications
======================

First of all, you'll need to say to Sphinx where the directory with your code 
is, relative to the :ref:`conf.py` file. This is done on the lines:

.. literalinclude:: ../../_static/conf.py
   :caption: conf.py lines 13 to 15
   :language: python
   :start-at: import os
   :end-at: sys.path.insert
   :lineno-start: 13

The line 48 adds the Sphinx default texts language for the project:

.. literalinclude:: ../../_static/conf.py
   :caption: conf.py lines 48 and 49
   :language: python
   :start-at: # Language
   :end-at: language
   :lineno-start: 48

Line 84 sets the theme of the documentation to be the 
`PyData Sphinx Theme <https://pydata-sphinx-theme.readthedocs.io/en/>`_. The 
same one used by 
`NumPy <https://numpy.org/doc/stable/>`_, 
`Jupyter <https://docs.jupyter.org/en/latest/>`_, 
`Matplotlib <https://matplotlib.org/stable/>`_, 
`Pandas <https://pandas.pydata.org/docs/>`_, 
`SciPy <https://docs.scipy.org/doc/scipy/>`_ 
and many other great projects *-so even if your project is not that great, I 
asure you that your documentation will be-*.

.. literalinclude:: ../../_static/conf.py
   :caption: conf.py line 84
   :language: python
   :start-at: html_theme
   :end-at: html_theme
   :lineno-start: 84


Customizing the theme
=====================

As you can see, the :ref:`conf.py` file ads a section for theme customization. 
You can find a full description of the configuration posibilities on the 
`User Guide <https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/index.html>`_.

The configuration lines regarding the configuration of the theme founded on the 
:ref:`conf.py` are divided into two main sections. Lines 94 to 97 configures 
the **left sidebar**,

.. literalinclude:: ../../_static/conf.py
   :caption: conf.py lines 94 to 97
   :language: python
   :start-at: # Sidebar configuration
   :end-at: }
   :lineno-start: 94

This code adds two items:

#. A search bar.
#. A bootstrap-friendly navigation section. When there are no pages to show, it
   dissapears.

On the other hand, lines 99 to 113 adds some **little tweaks**:

.. literalinclude:: ../../_static/conf.py
   :caption: conf.py lines 99 to 113
   :language: python
   :start-at: # General theme options
   :lineno-start: 99

* Line 102 sets the title of the documentation (on the left upper corner). In 
  this guide, the text logo is the same name used for the project: "Demorepo".
  Note that it can also be an image.
* Line 104 adds the light/black theme color switch and a icon bar with links to
  the upper navigation bar.
* Lines 105 to 113 configure the icons to display on the upper right corner, as
  you can see, a GitHub icon is added with a link to the repository of this 
  guide.


Extensions
==========

As it was discussed, Sphinx make use of extensions to add some functionalities 
to your documentation, such as automatic use of docstrings, autosummary of 
objects in files or syntaxis detection of syle (such as NumpyDocs). Some of 
this extensions come **built-in** with Sphinx and others are developed by
**third-parties**, which can be installed using ``pip``.

Here, we'll cover the extensions used on the :ref:`conf.py` file. As you can 
see the extensions used are listed on the lines 33 to 38:

.. literalinclude:: ../../_static/conf.py
   :caption: conf.py lines 33 to 38
   :language: python
   :start-at: extensions = [
   :end-at: ]
   :lineno-start: 33
   :name: extension-list

Extensions normally allow further configuration of its features, in the 
:ref:`conf.py` file, it can be found on the section from line 52 to 76:

.. literalinclude:: ../../_static/conf.py
   :caption: conf.py lines 52 to 76
   :language: python
   :start-at: # -- Extension config
   :end-at: myst_heading_anchors
   :lineno-start: 52
   :name: extension-config


Built-in extensions
-------------------

A rule of thumb to know which extensions are built-in with sphinx, is that its
names allways begin with ``sphinx.ext.NAME``, where ``NAME`` is the name of the
extension. On the config file, 3 built-in extensions are activated *(The first 
one explicitly becouse its in the list and the other two implicitly as their
activated by the use of the* ``numpydocs`` *extension)*:

.. seealso:: 
   A full list of Sphinx built-in extensions and links to its 
   documentations can be found 
   `here <https://www.sphinx-doc.org/en/master/usage/extensions/index.html#built-in-extensions>`_.


1. ``sphinx.ext.viewcode``
^^^^^^^^^^^^^^^^^^^^^^^^^^

This extension allow for the ``Show Source`` button to appear on the right 
sidebar. This extension does not have any extra configuration on the 
:ref:`extension-config`.

.. seealso::
   You can find further information of this extension on the 
   `viewcode documentation page <https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html>`_.


.. _sphinx-autosummary-section:

2. ``sphinx.ext.autosummary``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This extension generates function/method/attribute summary lists or files and 
its especially useful when your docstrings are long and detailed, and putting 
each one of them on a separate page makes them easier to read.

The configuration of this extension can be found on lines 71 to 73 on 
:ref:`extension-config`:

* ``autosummary_generate``: create `.rst` with a table with the objects inside 
  files summarized. The file can be generated passing a custom template.
* ``autosummary_generate_overwrite``: 

.. seealso::
   You can find further information of this extension on the 
   `autosummary documentation page <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_.

3. ``sphinx.ext.autodoc``
^^^^^^^^^^^^^^^^^^^^^^^^^

This extension import the modules you are documenting, and pull in 
documentation from docstrings in a automatic way.

.. warning:: Some common error founded when using ``autodoc`` is that the 
   extension is unable to import the modules or packages with your code. This
   behavior can be disabled on the ``conf.py`` file.

The configuration of this extension can be found on lines 59 to 69 on
:ref:`extension-config`:

*  ``autodoc_default_options``:

   The default options for autodoc directives. They are applied to all autodoc 
   directives automatically. 

*  ``members``: 
      autodoc will generate document for the members of the target module,
      class or exception (recursively)

*  ``undoc-members``:
      autodoc will not generate document for the members not having docstings

*  ``private-members``: 
      autodoc will also generate document for the private members

* ``autodoc_typehints``: 
   No typehints are shown.

.. seealso::
   You can find further information of this extension on the 
   `autodoc documentation page <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_.


Thrid-parties extensions
------------------------

These are the third party extensions used on the config file:

1. ``numpydoc``
^^^^^^^^^^^^^^^

This extension provides support for the Numpy docstring standard in Sphinx.

The configuration of this extension can be found on lines 54 to 57 on 
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

.. seealso::
   You can find more information about this extension in the 
   `NumpyDocs documentation <https://numpydoc.readthedocs.io/en/latest/index.html>`_.


2. ``myst-parser``
^^^^^^^^^^^^^^^^^^

This extension translates Markdown files to reStructuredText files, allowing 
for the use of `.md` files into your documentation. An example of this can be 
found on the use of the file 
:doc:`How to write DocStrings <../_styleguides/docstrings-guidelines>`. 
Possibly you didn't even notice, but if you see the source code you'll see 
**its a Markdown file!**

The only configuration on the :ref:`extension-config` regarding this extension
is found on line 76. ``myst_heading_anchors`` is used only for Markdown header
references inside file, such as ``[link to header](#SOME-HEADER)`` to work.

.. seealso::
   You can find more information about this extension in the 
   `MyST Parser documentation <https://myst-parser.readthedocs.io/en/latest/index.html>`_.

3. ``sphinx-design``
^^^^^^^^^^^^^^^^^^^^

This extension adds several UI components and provide extra flexibility for 
content creation. These include badges, buttons, cards, and tabs, among other 
components.

.. seealso::
   You can find more information about this extension in the 
   `Sphinx Design documentation <https://sphinx-design.readthedocs.io/en/latest/index.html>`_.