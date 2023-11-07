===================
Initializing Sphinx
===================

First of all, you'll need to initialize Sphinx in this project. For that, 
create a `docs` directory. Your dirtree must look like this:

.. code-block:: none
    :caption: Original dir tree
    :name: original-dir-tree

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

Then initialize Sphinx inside the `docs` directory using:

.. code-block:: bash

    sphinx-quickstart

This command will ask you for:

#. ``> Separate source and build directories (y/n) [n]:`` y

#. ``> Project name:`` Normally the same as the git repo

#. ``> Author names(s):`` The authors of the code developed

#. ``> Project release []:`` Version name such as 1.0, Alpha, etc.

#. ``> Project languaje [en]:`` en

After this you'll have the following dirtree inside `docs`:

```
.. code-block:: none
    :caption: Dir tree after Sphinx init
    :name: dir-tree-after-sphinx-init
    
    docs/
    ├── build/
    └── source/
        ├── _static/
        ├── _templates/
        ├── conf.py
        └── index.rst
    Makefile
    make.bat

The `source` directory contains a collection of plain-text document sources and 
the configuration file `conf.py`, where you can configure all aspects of how 
Sphinx reads your sources and builds your documentation.

The `build` directory contains the automathic generated documentation in the 
format that you specified in the `conf.py` file (for example html, LaTeX, etc).

To make life easier, some Makefiles are also in the directory. These implement 
an standard way to building the documentation.