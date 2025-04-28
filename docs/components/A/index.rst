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


todos:

-  filter

