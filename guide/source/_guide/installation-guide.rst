==================
Installation guide
==================

Clone the repository
====================

To use this guide, you'll need to clone the repository that contains the source
code from Github.

.. code-block:: bash

   git clone https://github.com/ecastroth/ultimate-sphinx-tutorial.git


Install the dependencies
========================

Once the repository is in your machine, you have to install its dependencies. 


Install the dependencies with ``conda``
---------------------------------------

If you want to install a full ``conda`` environment you can do:

.. code-block:: bash

   conda env create -f requirements/conda-requirements.yaml

Once the dependencies are installed, activate the env using:

.. code-block:: bash

   conda activate sphinx-demo

And you're good to go! Move on to the 
:doc:`Docstring guide <_styleguides/docstrings-guidelines>`.


Install the dependencies with ``pip``
-------------------------------------

If you want to install the dependencies with ``pip`` you can do:

.. code-block:: bash

   pip install -r requirements/pip-requirements.yaml

And you're good to go! Move on to the 
:doc:`Docstring guide <_styleguides/docstrings-guidelines>`.