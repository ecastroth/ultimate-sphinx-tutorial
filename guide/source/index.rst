.. Getting started with Sphinx documentation master file, created by
   sphinx-quickstart on Mon Nov  6 22:00:38 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

The final Sphinx tutorial
=========================

Welcome!

This html files contain a full tutorial on how to use Sphinx to document a 
project *-with explanations for nested directoires, something I struggle with
when I was learning how to use this tool-*, embed Markdown files, work with 
extensions and building a beautifull documentation for your project.

I hope this documentation will be useful to your journey learning Sphinx. I've
try my best to make this the more detailed possible and intuitive possible, 
however if you feel that something can be improved feel free to contact me at
`my email <ecastroth@gmail.com>`_.

You can find the guides for writting docstrings and implementing Sphinx to your
project below. Enjoy!

.. toctree::
   :maxdepth: 1
   :hidden:

   _guide/_styleguides/docstrings-guidelines
   _guide/_tutorial/sphinx-in-your-project


.. grid::

   .. grid-item-card:: 
      :text-align: center
      :shadow: sm

      **Docstrings primer**
      ^^^^^^^^^^^^^^

      This section states how to write docstrings in your code in a way that 
      Sphinx can recognize them automatically.

      ++++++++++

      .. button-ref:: _guide/_styleguides/docstrings-guidelines
         :color: primary
         :expand:

         To the Docstring primer

   .. grid-item-card::
      :text-align: center
      :shadow: sm

      **Adding Sphinx**
      ^^^^^^^^^^^^^^^^^

      This section explains step-by-step how to add Sphinx to your project, how 
      to configurate it and use it to build beautifull documentation.

      ++++++++++

      .. button-ref:: _guide/_tutorial/sphinx-in-your-project
         :color: primary
         :expand:

         To Adding Sphinx
