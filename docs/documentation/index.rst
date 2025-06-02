#############
Documentation
#############

Here we want to show how to have the same element multiple times in the Documentation.


**Howto:**

You do have to patch your conf.py to get this working:

.. literalinclude:: /conf.py
   :caption: Changes in conf.py
   :language: py
   :lineno-match:
   :start-after: # changes for needs_id_prefixes


**Filter:**

You can easily filter for the current file with https://sphinx-needs.readthedocs.io/en/latest/filter.html#filtering-for-needs-on-the-current-page

It is even possible to use the new introduced filter:

.. code-block:: python

   .. needtable:: Table of elements within this prefix area
      :show_filters:
      :filter: c.this_prefix()

The `this_prefix` does support elements which are not part of any prefix.


**Fixing Document Headline:**

Example:

.. literalinclude:: /components/index.rst
   :caption: How-to fix headlines in a toctree
   :language: py
   :lineno-match:

Todo: test if it working with child headlines, too.

**Working Features:**

-  needs
-  needpart
-  embedded needs
-  links between needs, needparts and embedded needs
-  filtering with needtable
-  filtering with needlist
-  filtering with needflow
-  use needimport
-  use needextend
-  use sphinx-test-reports

**Restrictions:**

-  This methodology is not working with needpie, see https://github.com/useblocks/sphinx-needs/issues/1449.
-  This methodology is not working with needbar, see https://github.com/useblocks/sphinx-needs/issues/1449.
-  This methodology is not tested with needarch.
-  This methodology is not tested with needuml.
-  This methodology is not tested with needextract.
-  This methodology is not tested with needservice.
-  This methodology is not tested with list2need.
-  This methodology is not tested with needgantt.
-  This methodology is not tested with needsequence.
-  We currently do not have an easy way to filter for elements in a dedicated file location
