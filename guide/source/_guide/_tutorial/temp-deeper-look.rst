=================================
Deeper look on the template files
=================================

So, the custom template files I recommend in 
:doc:`Adding and using Sphinx in your project <to-the-next-level>`
are:

.. literalinclude:: ../../_static/_templates/custom-module-template.rst
   :caption: custom-module-template.rst
   :language: rst
   :lineno-start: 1
   :name: custom-module-template.rst

.. literalinclude:: ../../_static/_templates/custom-object-template.rst
   :caption: custom-object-template.rst
   :language: rst
   :lineno-start: 1
   :name: custom-object-template.rst

As you can see, the template files are reStructuredText files written using the
`Jinja templating engine <https://jinja.palletsprojects.com/en/3.1.x/>`_  
syntaxis and reStructuredText. They contain the instructions to automatically 
document any file.

.. seealso::

   #. `Sphinx support for Jinja syntaxis <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html#customizing-templates>`_
   #. `Jinja Template Designer Documentation <https://jinja.palletsprojects.com/en/3.1.x/templates/>`_
   #. `Sphinx templating documentation <https://www.sphinx-doc.org/en/master/development/templating.html>`_


Primer on the syntaxis
======================

First of all, we need to understand some basics of the syntaxis used on the
Template files.


Jinja syntaxis
--------------

First of all its important to undestand the importance of Jinja delimiters. 
There are three of them:

*  ``{% ... %}`` for **statements**.
*  ``{{ ... }}`` for **expressions** to print to the template output.
*  ``{# ... #}`` for **comments** not included in the template output.

Maybe the more important of these is the statements syntaxis, as they allow for
neat things such as:

*  **if statements**:

   The if statement in Jinja is comparable with the Python if statement.

   .. code-block:: rst
      
      {% if kenny.sick %}
         ...
      {% elif kenny.dead %}
         ...
      {% else %}
         ...
      {% endif %}


*  **for statements**:

   The for statements in Jinja works somewhat like Python for statements, the 
   most important differences are that dictionaries are not sorted by default 
   and the ``break`` and ``continue`` don't work.

   .. code-block:: rst
      
      {% for user in users %}
         ...
      {% endfor %}

*  Many other! Check out the 
   `list of control structures <https://jinja.palletsprojects.com/en/3.1.x/templates/#list-of-control-structures>`_.


Jinja filters
-------------

With Jinja you can also use filters, similar to the way you use pipelines on
Unix systems. For example, this prints the uppercase of the first letter of a 
variable 

.. code-block:: rst

   {{ variable[0] | upper }}

You can find a full list of the built-in filters 
`here <https://jinja.palletsprojects.com/en/3.1.x/templates/#list-of-builtin-filters>`_.


Sphinx global variables for Jinja
---------------------------------

On the other hand, Sphinx support the following global variables to be used 
with Jinja syntaxis, all of them can be "called" vía 
``{ sphinx_global_variable }`` or  ``{{ sphinx_global_variable }}`` if you want
to print them in the template.

*  ``name``: Name of the documented object, excluding the module and class 
   parts.

*  ``objname``: Name of the documented object, excluding the module parts.

*  ``fullname``: Name of the documented object, including the module and class
   parts.

*  ``module``: Name of the module the documented object belongs to.

*  ``underline``: A string containing ``len(full_name) * '='``. Use the 
   ``underline`` filter instead.

*  ``attributes``: List containing names of “public” attributes in the 
   class/module. Only available for classes and modules.

*  ``functions``: List containing names of “public” functions in the module. 
   Here, “public” means that the name does not start with an underscore. 
   Only available for modules.

*  ``classes``: List containing names of “public” classes in the module. Only 
   available for modules.

*  ``modules``: List containing names of “public” methods in the class. 
   Only available for classes.

*  ``exceptions``: List containing names of “public” exceptions in the module. 
   Only available for modules.


Understanding the Template files
================================

To fully understand the template files, we will analyze them separately and 
separate them into each of their sections.

The object template file
------------------------

The :ref:`object template file <custom-object-template.rst>` is the simplest of
the two templates that we will analyze. It can be divided into the three main 
sections highlighted below:

.. literalinclude:: ../../_static/_templates/custom-object-template.rst
   :caption: custom-object-template.rst
   :language: rst
   :lineno-start: 1
   :emphasize-lines: 1-2, 6-8, 10-

Suppose that a function ``example_function()`` is going to be documented with
this template, then: 

.. literalinclude:: ../../_static/_templates/custom-object-template.rst
   :caption: custom-object-template.rst lines 1 and 2
   :language: rst
   :lineno-start: 1
   :end-at: {{ underline }}
   :name: template-titlelines

Print the title of the file: 

*  **Line 1** prints out the name of the object (in this case 
   "example_function"), then adds a space and print the object type formatted 
   (in this case "function") with the first letter uppercased and the rest 
   without changes.
*  **Line 2** adds a underline of ``=`` with the lenght of the string, making 
   it a section.

.. literalinclude:: ../../_static/_templates/custom-object-template.rst
   :caption: custom-object-template.rst lines 6 to 8
   :language: rst
   :start-at: {% if objtype == 'function' %}
   :end-at: {% endif %}
   :lineno-start: 6

Check out if the object is a function, in that case, prints out its docstrings.
(this would been print out in our ``example_function()`` case)

.. literalinclude:: ../../_static/_templates/custom-object-template.rst
   :caption: custom-object-template.rst lines 10 onwards
   :language: rst
   :start-at: {% if objtype == 'class' %}
   :lineno-start: 10

Check out if the object is a class, in that case, prints out its docstrings 
showing its methods, inheritance and its inherited members (this would not 
print anything in our ``example_function()`` case)


The module template file
------------------------

The :ref:`module template file <custom-module-template.rst>` can be divided 
into the following main sections highlighted below:

.. literalinclude:: ../../_static/_templates/custom-module-template.rst
   :caption: custom-module-template.rst
   :language: rst
   :lineno-start: 1
   :emphasize-lines: 1-2, 4-5, 7-17, 19-30, 32-43, 45-55, 57-69

If you notice, the first two lines are the same as the 
:ref:`template-titlelines` in the previous file so I'll omit them from the 
explanation.

On the other hand, lines 4 and 5 get the docstrings of the module, nevertheles
the ``:no-members:`` flag prevents that any of the objects docstrings (either 
attributes, functions, etc) get printed out in the file, so **this lines only 
print out the module-level docstrings**.

The further blocks of code, do all the same but for different elements inside 
the module (if you note, the structure of lines 7 to 17 is the same as 19 to 30
or 32 to 43 and so on) so we'll be focusing only on one of them.

.. literalinclude:: ../../_static/_templates/custom-module-template.rst
   :caption: custom-module-template.rst
   :language: rst
   :start-at: {% block functions %}
   :end-at: {% endblock %}
   :lineno-start: 1

The ``block`` tag **in simple words** calls or defines a child template to take
its place. In this case, the child template is defined inside the block in 
lines 2 to 11.

The ``if`` statement is here to only build the block if the type of object is
present inside the module (in this case "functions"). Line 3 creates a 
paragraph heading that is not used to create a TOC node.

Finally, lines 5 to 10 creates a ``autosummary`` table generating a page for 
every element (in this case every function in the module) using the 
:ref:`custom-module-template.rst` template file.