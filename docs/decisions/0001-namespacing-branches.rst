Namespacing Branches and Tags
#############################

Status
******

Draft

Context
*******

This ADR was written in response to this `Discourse thread`_.

Currently, 2U continuous delivery tooling creates branches and tags
in the repository "global namespace."  By that I mean that branches
and tags have the form ``release`` or ``release-candidate-3729``.
This is confusing because those branches and tags appear to be global,
officially sanctioned by the project, and authoritative.

A result of this is that the official named releases of the platform
require a namespace specifier, for example,
``open-release/olive.master``.

This is confusing to most members of the community and reflects the
prior stewardship arrangements for the project.

It is not typical of open-source projects to allow participating
organizations to push organization specific branches and tags to the
canonical upstream.  However, we recommend not prohibiting this at this
time.  There are two reasons for that:

1. This would require more substantial changes to participant deployment
   systems that would delay getting value from this initial change.
2. The 2U branches and tags represent code that is battle-tested in
   production at scale and are, thus, valuable sign posts for
   community members.

.. _Discourse thread: https://discuss.openedx.org/t/should-we-rename-the-release-branches/8827/7


Decisions
*********

1. We will *not* forbid project participants with write access to
   repositories from pushing branches or tags to the canonical
   upstream hosted at the openedx GitHub organization.
2. However, we *will* require that project participants namespace their
   upstream branches and tags to clarify their origin and purpose.
3. The global namespace will be reserved for global project purposes.
4. Branches within *forks* of Open edX repositories may choose to follow this
   guidance, but they do not need to.

Going forward, branches and tags that originate from any specific
organization or user participating in the Open edX project must by namespaced
as follows:

* ``$ORGANIZATION/$PURPOSE`` for organizations.
* ``$GITHUB_USER/$PURPOSE`` for userers.

For example:

* ``acme/release``
* ``acme/release-candidate-3729``
* ``acme/our-feature``
* ``e0d/my-feature``

In some cases, multiple namespaces may be appropriate. For example, ``e0d``
may be working for ``acme`` on a project funded by ``wile-e-coyote``. When in
doubt, one should choose the namespace which best informs community who manages
the branch, which in this case would be either ``e0d`` or ``acme``.

In the case of the global namespace, tags and branches may still be
further qualified to provide additional information and specificity.

For example:

* ``release`` would be considered in the global namespace.
* ``release/redwood`` would represent the branch for an officially-
  sanctioned Open edX named release.


Consequences
************

#. Continuous delivery systems and other automation should be updated
   across the ecosystem to use the proper naming convention for
   branches and tags. Existing branches and tags should be updated to use the
   new naming protocol. Axim will announce this to community members.
#. Axim will ensure that branch namespacing is communicated to new developers
   via onboarding documentation.
#. Axim may prune newly-created branches and tags which don't use a proper
   namespace.
#. Axim will announce its intent to remove batches of existing branches and
   tags that don't use namespaces. Each batch will include a reasonable grace
   period.
