###########
Component A
###########

.. sw_req:: Example Software Requirement
   :id: SWRQ_EXAMPLE_SW_REQUIREMENT

   empty

.. sw_req:: Secound Example Software Requirement
   :id: SWRQ_EXAMPLE_2_SW_REQUIREMENT

   :np:`(reqpart) example text`

.. sw_req:: Embedded Parent Example Software Requirement
   :id: SWRQ_EMBEDDED_PARENT_EXAMPLE_SW_REQUIREMENT

   empty

   .. sw_req:: Embedded Child Example Software Requirement
      :id: SWRQ_EMBEDDED_CHILD_EXAMPLE_SW_REQUIREMENT

      empty

.. comp:: Example comp
   :id: C_EXAMPLE
   :satisfies: SWRQ_EXAMPLE_SW_REQUIREMENT, SWRQ_EXAMPLE_2_SW_REQUIREMENT.reqpart,
               SWRQ_EMBEDDED_PARENT_EXAMPLE_SW_REQUIREMENT, SWRQ_EMBEDDED_CHILD_EXAMPLE_SW_REQUIREMENT

   empty

.. needtable:: Table of sw_req
   :filter: c.this_doc() and type == 'sw_req'

.. needpie:: Pie chart of ratio sw_req / comp

   type == 'sw_req' and c.this_doc()
   type == 'comp'
