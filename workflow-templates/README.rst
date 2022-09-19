Workflow Templates
##################

These are `templates for GitHub Actions workflows`_ that can be added to different repositories across the openedx GitHub organization.

To use these in your repository: 

* go to the **Actions** tab in your repository,
* click **New Workflow**,
* scroll down to **by Open edX**, and
* click **Configure** on your selected template.

Please Note
***********

#. When adding a template-based workflow, use the GitHub UI, following the instructions above. Do not copy the template workflow into you repository, since there are template-specific variables (for example, ``$default-branch``) that will not be resolved when used as a real repository workflow.

#. These should *not* be confused with `our shared workflows`_, which are centrally stored each as a single copy, and can be *referenced* by different workflows through the openedx GitHub organization.


.. _templates for GitHub Actions workflows: https://docs.github.com/en/actions/using-workflows/creating-starter-workflows-for-your-organization
.. _our shared workflows: https://github.com/openedx/.github/tree/master/.github/workflows
