Namespacing Branches and Tags
#############################

Status
******

Draft

Context
*******

This ADR was written in response to this `Discourse thread`_.

Currently, 2U continuous delevery tooling creates branches and tags
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

1. We will not forbid project participants with write access to
   repositories from pushing branches or tags to the canonical
   upstream hosted at the openedx GitHub organization
2. We will require that project participants namespace their branches
   and tags to clarify their origin and purpose
3. The global namespace will be reserved for global project purposes

Going forward branches and tags that originate from any specific
organization partipatinging in the Open edX project must by namespaced
as follows:

``acme/release``

or

``acme/release-candidate-3729``

In the case of the global namespace, tags and branches may still be
further qualified to provide additional information and specificity.

For example:

``release`` would be consider in the global namespace.

``release/palm`` would represent the branch for an officially
sanctioned Open edX named release.


Consequences
************

1. Continuous delivery systems and other automation should be updated
   across the ecosystem to use the proper naming convention for
   branches and tags
2. Existing branches and tags should be updated to use the new naming
   protocol
3. A reasonable grace period should be established to schedule and
   complete the required work
