#########
Component
#########

**Introdction**

<Here we give a short introdction to :need:`C_EXAMPLE`.>

**Requirements**

.. sw_req:: Example Software Requirement
   :id: SWRQ_EXAMPLE_SW_REQUIREMENT
   :derived: SYSRQ_EXAMPLE_SYS_REQUIREMENT

   :need:`C_EXAMPLE` shall <added your text here>.

.. sw_req:: Secound Example Software Requirement
   :id: SWRQ_EXAMPLE_2_SW_REQUIREMENT

   :need:`C_EXAMPLE` shall <added your text here>.

   :np:`(needpart) example text`

   Important is to cover additionally :need:`SWRQ_EXAMPLE_2_SW_REQUIREMENT.needpart`.

.. sw_req:: Embedded Parent Example Software Requirement
   :id: SWRQ_EMBEDDED_PARENT_EXAMPLE_SW_REQUIREMENT

   :need:`C_EXAMPLE` shall <added your text here>.

   Important is to cover additionally :need:`SWRQ_EMBEDDED_CHILD_EXAMPLE_SW_REQUIREMENT`.

   .. sw_req:: Embedded Child Example Software Requirement
      :id: SWRQ_EMBEDDED_CHILD_EXAMPLE_SW_REQUIREMENT

      :need:`C_EXAMPLE` shall <added your text here>.

**Architecture Element**

.. comp:: Example comp
   :id: C_EXAMPLE
   :part_of: LIB_EXAMPLE
   :satisfies: SWRQ_EXAMPLE_SW_REQUIREMENT, SWRQ_EXAMPLE_2_SW_REQUIREMENT.needpart,
               SWRQ_EMBEDDED_PARENT_EXAMPLE_SW_REQUIREMENT, SWRQ_EMBEDDED_CHILD_EXAMPLE_SW_REQUIREMENT

   <Here you document your component.>

**Reports**

.. needtable:: Table of sw_req within in this file
   :filter: c.this_doc() and type == 'sw_req'

.. needtable:: Table of elements within this prefix area
   :filter: c.this_prefix()

List of elements within this prefix area:

.. needlist::
   :filter: c.this_prefix()

We cannot use c.this_doc() in needpie and needbar, see https://github.com/useblocks/sphinx-needs/issues/1449.

.. needpie:: Pie chart of ratio sw_req / comp

   type == 'sw_req'
   type == 'comp'

.. needflow:: Test needflow
   :filter: c.this_prefix()

Let's try to import needs via `needimport`:

.. needimport:: /_static/_external_data/example_needs.json
   :id_prefix: imp_
   :tags: imported

Show how to use `needextend`:

.. needextend:: "imported" in tags and c.this_prefix()
   :status: implemented

Filter for imported needs with `needtable`:

.. needtable:: Imported Needs
   :show_filters:
   :filter: "imported" in tags and c.this_prefix()

.. test-file:: Example for Test Results
   :file: _static/_external_data/merge_dicts_test_results.xml
   :id: TF_EXAMPLE
   :auto_suites:
   :auto_cases:
