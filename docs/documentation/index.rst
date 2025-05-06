#############
Documentation
#############

Here we want to show how to have the same element multiple times in the Documentation.


**Howto:**

You do have to patch your conf.py to get this working:

.. literalinclude:: conf.py
   :caption: Changes in conf.py
   :language: py
   :lineno-match:
   :start-after: # changes for needs_id_prefixes


**Filter:**

You can easily filter for the current file with https://sphinx-needs.readthedocs.io/en/latest/filter.html#filtering-for-needs-on-the-current-page

It is even possible to use the new intoduced filter:

.. code-block:: python
   .. needtable:: Table of elements within this prefix area
      :show_filters:
      :filter: c.this_prefix()

**Fixing Document Headline:**

Example:

.. literalinclude:: components/index.rst
   :caption: How-to fix headlines in a toctree
   :language: py
   :lineno-match:

Todo: test if it working with child headlines, too.

**Restrictions:**

-  This methodology is not working with needextend.
-  We currently do not have an easy way to filter for elements in a dedicated file location
