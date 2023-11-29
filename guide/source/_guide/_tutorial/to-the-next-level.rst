===========================
Taking it to the next level
===========================

Changing the ``source`` directory tree
======================================

First of all, its important to note that the files builded using the 
``sphinx-apidoc`` command serves (for an advance user) as a starting point for 
building the final documentation, **not as the end files of it**. So lets 
modify this files to give the documentation a better look.

First of all I dont like at all the distribution of the files, so we'll add a
directory structure with the main parts of any documentation:

*  **User guide:** This directory of the documentation will contain files 
   explaining how to use the user intended scripts of the project.

*  **API Reference:** On the other hand, some users may need an insight on the
   specific documentation of a object. All the files with the docstrings of 
   your code/source files build up the API Reference part of the documentation. 

With this structure on mind, we'll modify the directories in the source 
directory to this:

.. code-block:: none
   :caption: docs dirtree

   build/
   source/
   ├── _apireference/
   ├── _static/
   ├── _templates/
   └── _userguide/
   conf.py
   index.py

Where the ``_userguide`` directory was created and the ``_component_autodoc`` 
change its name to ``_apireference`` (this will be explained on the
:ref:`API Reference <apireference-section>` section).


Adding the User guide
=====================

First of all, we'll populate the User guide. On this example we will add 3 
files to the ``_userguide`` directory:

1. **Introduction file**

   This file is the landing page of the user guide and must link to other 
   important files. Also, it states the scope of the guide.

   .. literalinclude:: ../../_static/_userguide/introduction.rst
      :caption: _userguide/introduction.rst
      :language: rst
      :lineno-start: 1

2. **Some quickstart file**

   This file is only a example of a quickstart tutorial.

   .. literalinclude:: ../../_static/_userguide/quickstart1.rst
      :caption: _userguide/quickstart1.rst
      :language: rst
      :lineno-start: 1

3. **Other quickstart file**

   This file is only a example of a quickstart tutorial.

   .. literalinclude:: ../../_static/_userguide/quickstart2.rst
      :caption: _userguide/quickstart2.rst
      :language: rst
      :lineno-start: 1

.. note:: Try to add the ``introduction.rst`` file to the documentation before
   proceeding with the guide. If you notice, is the only file needed as it 
   allready have links to the other quickstart files.


.. _apireference-section:

Modifiying the API Reference
============================

If you are familiarized with documentation, you've notice that the 
documentation we build on the 
:doc:`Adding Shinx to your project <sphinx-in-your-project>` part of this 
tutorial **is** the API Reference part of the documentation (hence the change
of the directory name). Nevertheless it can be much better than it is. To 
accomplish this we'll make use of the
:ref:`Autosummary extension <sphinx-autosummary-section>`.

With this extension, we'll generate a documentation that have a page for every
file (also known as module) with its file-level docstrings and a summary list 
of every ``function``, ``class`` and ``exception`` objects in the module, with
links to a separate page (one for every object) with its docstrings.


The templates
-------------

To make your life easier, I build the following two template files that you'll 
have to simply put on the ``_templates`` directory. 

1. **Module template:** 

   This one handles the automatic documentation of the modules.

   .. literalinclude:: ../../_static/_templates/custom-module-template.rst
      :caption: _templates/custom-module-template.rst
      :language: rst
      :lineno-start: 1

2. **Object template:**

   This other one handles how the classes and functions pages will be 
   documentated:

   .. literalinclude:: ../../_static/_templates/custom-object-template.rst
      :caption: _templates/custom-object-template.rst
      :language: rst
      :lineno-start: 1

If you want to know how this files work, you can read the tangent on 
:doc:`deeper look on template files <temp-deeper-look>`.


Modifiying the ApiDoc files
---------------------------

So, now that we have the templates, lets modify the files on the now 
``_apireference`` directory *(ex* ``_component_autodoc`` *)*. We'll make the 
following changes:

#. Remove the ``modules.rst`` and ``component.rst`` as we'll create our own 
   landing page for this section.

#. Create the landing page file for the API Reference with the following 
   content:

   .. literalinclude:: ../../_static/_apireference/introduction.rst
      :caption:  _apireference/introduction.rst
      :language: rst
      :lineno-start: 1
      :emphasize-lines: 18, 20-24

   This file links to the files or packages inside the component project, that 
   is the ``file1.rst`` file and the ``package1`` package.

   Note that we have used the ``autosummary`` extension with the template that 
   we created to document the code inside the ``file1.rst`` file. For this, 
   we've explicitly said to Sphinx that we are in the component module 
   (line 18) and that we want that uses the template for modules we've built 
   (line 21). The generated files will be saved under the ``_generated`` directory inside
   the current directory (``_apireference``).

   .. note::
      Try to add this file to the ``index.rst`` to see how the ``autosummary``
      extension built the documentation for the ``file1.rst`` file.

#. Lets document the other elements of the project using the ``autosummary`` 
   extension modifiying the code inside the ``component.package1.rst``,
   ``component.package1.subpackage1.rst`` and 
   ``component.package1.subpackage2.rst`` files. Note that no other file will 
   be created by hand because of the use of the extension that will do it for 
   us.

   *  **The Package 1 file:**

      This file represent the ``package1`` directory and all the elements 
      inside it. So it must have two sections, one for the modules (or files) 
      and one for the subpackages.

      .. literalinclude:: ../../_static/_apireference/component.package1.rst
         :caption:  _apireference/component.package1.rst
         :language: rst
         :lineno-start: 1

      Note that the files are documented analogously to the ``file1.rst`` and
      the subpackages files are linked.

   *  **The SubPackage 1 file:**

      This file represent the ``subpackage1`` directory and all the elements 
      inside it. So it must have only one section for its modules.

      .. literalinclude:: ../../_static/_apireference/component.package1.subpackage1.rst
         :caption:  _apireference/component.package1.subpackage1.rst
         :language: rst
         :lineno-start: 1

   *  **The SubPackage 2 file:**

      This file represent the ``subpackage2`` directory and all the elements 
      inside it. So it must have only one section for its modules.

      .. literalinclude:: ../../_static/_apireference/component.package1.subpackage2.rst
         :caption:  _apireference/component.package1.subpackage2.rst
         :language: rst
         :lineno-start: 1
      
   Note that this files are also much shorter than the original ones. 


Updating and upgrading the ``index.rst``
========================================

The ``index.rst`` is the face of your documentation and if you haven't modified
it from the previous section now is broken because we have modified the dirtree

Taking advantage of the fact that we are going to modify it, we can improve it
adding a little more text and some cards with buttons linking to the main 
sections of the documentation:

.. literalinclude:: ../../_static/better-index.rst
   :caption: index.rst
   :language: rst
   :lineno-start: 1
   :emphasize-lines: 20-25, 28-

Note that the TOCTree is hidden so it only serves the purpose of indicate the 
file hierarchy. The files will be linked using buttons inside cards, which are 
built on the lines from 28 onwards. Give them a look!