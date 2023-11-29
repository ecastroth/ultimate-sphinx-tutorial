.. demorepo documentation master file, created by
   sphinx-quickstart on Wed Nov  8 11:40:43 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Demorepo's documentation!
====================================

This is an example text, imagine all the this that you can say on the landing 
page of your documentation! 

If you look online what are the most common documentation areas, you'll see
that the most of them have at least an **User guide**, with a guide explaining 
some features of the project and a **API Reference** with the documentation 
details for every function, class or object.

In this landing page, we'll add links to this two bigger areas of the
documentation. Feel free to explore!

.. toctree::
   :maxdepth: 1
   :hidden:

   _userguide/introduction
   _apireference/introduction


.. grid::

   .. grid-item-card:: 
      :text-align: center
      :shadow: sm

      **User guide**
      ^^^^^^^^^^^^^^

      The user guide provides in-depth information on the key concepts of the
      features with useful background information and explanation.

      ++++++++++

      .. button-ref:: _userguide/introduction
         :color: primary
         :expand:

         To the User guide

   .. grid-item-card::
      :text-align: center
      :shadow: sm

      **API Reference**
      ^^^^^^^^^^^^^^^^^

      The reference guide contains a detailed description of the functions, 
      modules, and objects included in this project.

      ++++++++++

      .. button-ref:: _apireference/introduction
         :color: primary
         :expand:

         To the API Reference
