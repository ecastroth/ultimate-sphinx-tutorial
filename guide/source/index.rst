.. Getting started with Sphinx documentation master file, created by
   sphinx-quickstart on Mon Nov  6 22:00:38 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

The ultimate Sphinx tutorial
============================

Welcome!

This html files contain a full tutorial on how to use Sphinx to document a 
project *-with explanations for nested directoires, something I struggle with
when I was learning how to use this tool-*, embed Markdown files, work with 
extensions and building a beautifull documentation for your project.

I hope this documentation will be useful to your journey learning Sphinx. I've
try my best to make this the more detailed possible and intuitive possible, 
however if you feel that something can be improved feel free to contact me at
`my email <ecastroth@gmail.com>`_.

You can find the guides for installing the necessary elements of the guide, 
writting code and docstrings, implementing Sphinx to your project and uploading
it to Read the Docs below. Enjoy!

.. toctree::
   :maxdepth: 1
   :hidden:

   _guide/installation-guide
   _guide/_styleguides/introduction
   _guide/_tutorial/sphinx-in-your-project
   _guide/rtd-support


.. grid::

   .. grid-item-card:: 
      :text-align: center
      :shadow: sm

      **Installation guide**
      ^^^^^^^^^^^^^^^^^^^^^^

      This section states how to install all the necessary dependencies to 
      follow the guide.

      ++++++++++

      .. button-ref:: _guide/installation-guide
         :color: primary
         :expand:

         To the Installation guide


   .. grid-item-card:: 
      :text-align: center
      :shadow: sm

      **Style guidelines**
      ^^^^^^^^^^^^^^^^^^^^

      This section contains the guidelines for writting more understandable 
      code and docstrings that can be recognized by Sphinx automatically.

      ++++++++++

      .. button-ref:: _guide/_styleguides/introduction
         :color: primary
         :expand:

         To the Style guidelines


.. grid::

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


   .. grid-item-card:: 
      :text-align: center
      :shadow: sm

      **Using Read the Docs**
      ^^^^^^^^^^^^^^^^^^^^^^^

      This section teach you how to upgrade your documentation uploading it to
      Read the Docs without giving it access to your GitHub account but not 
      lossing automatic updates.

      ++++++++++

      .. button-ref:: _guide/rtd-support
         :color: primary
         :expand:

         To using Read the Docs

