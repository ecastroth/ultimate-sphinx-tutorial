{{ name }} {{ objtype[0]|upper }}{{ objtype[1:] }}
{{ underline }}

.. currentmodule:: {{ module }}

{% if objtype == 'function' %}
.. autofunction:: {{ objname }}
{% endif %}

{% if objtype == 'class' %}
.. autoclass:: {{ objname }}
   :members:
   :show-inheritance:
   :inherited-members:
{% endif %}
