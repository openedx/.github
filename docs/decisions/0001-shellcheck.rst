
Adopt ShellCheck for shell script linting
#########################################

Status
******

**Accepted**

Initial implementation PRs:

* https://github.com/openedx/.github/pull/64
* https://github.com/openedx/edx-platform/pull/31809

Context
*******

Background
==========

Although Python is the preferred language for backend development in the Open edX ecosystem, there are a few circumstances in which shell scripting (generally: Bash) is a superior tool. In particular, developers may reach for shell scripting languages when one or more of the following is true:

* A consistent Python environment is not guaranteed.
* Requiring a Python environment would make the surrounding process (a build, a deployment pipeline, etc) less efficient.
* The operation is centered around moving or copying files, transforming text streams, or otherwise using standard POSIX tools.

In spite of these benefits, `shell scripting is notoriously fraught with pitfalls <https://mywiki.wooledge.org/BashPitfalls>`_, and many Open edX developers will have less experience writing shell scripts than they do writing Python or JavaScript. So, it is understood that shell script usage should be limited to specific scenarios.

In almost all repositories, Open edX Python code is checked for common mistakes using pylint. Many repositories go further and use static analysis tools such as pycodestyle, pydocstyle, mypy, black, and isort. In contrast, even in spite of the known difficulty of correct shell scripting, Open edX shell scripts are *not* currently checked with any static analysis tools. Therefore, as shell scripts continue to be used in new Open edX contexts like `translations tooling <https://github.com/openedx/openedx-atlas>`_ and `static asset tooling <https://github.com/openedx/edx-platform/pull/31790>`_, we would like to identify a verification tool and encourage Open edX developers to use it.

ShellCheck
==========

`ShellCheck <https://shellcheck.net>`_ seems very suitable:

* It is well-known, with over 31.5k stars on GitHub. Pylint, in comparison, has 4.5k.
* Its error codes, including suggested resolution steps, are `documented on its wiki <https://www.shellcheck.net/wiki/SC1000>`_.
* It can be installed in one line from various `common package managers <https://github.com/koalaman/shellcheck#user-content-installing>`_ including apt and homebrew.
* It can be integrated with `common editors <https://github.com/koalaman/shellcheck#user-content-in-your-editor>`_ including Vim and VSCode.
* As of the writing of this ADR, it `seems to be actively maintained <https://github.com/koalaman/shellcheck/commits/master>`_.

Finally, as a personal anecdote: ShellCheck has been extremely helpful to this ADR's author in `rewriting the edx-platform asset build in Bash <https://github.com/openedx/edx-platform/pull/31791>`_. In addition to catching simple mistakes like typos, ShellCheck's detailed error pages have provided understanding of important shell concepts such as `globbing and word splitting <https://www.shellcheck.net/wiki/SC2086>`_.

Decision
********

Open edX developers are encouraged to use ShellCheck as part of the CI suite for repositories containing shell scripts.

Consequences
************

* A configurable ShellCheck workflow template will be added to this repository. This will let developers add ShellChecking to their repository's PRs with a couple clicks.

  * To support deterministic builds, the template will allow repositories to independently pin ShellCheck to a specific version. We will encourage maintainers of these repositories to update their pin over time. We expect that this will lead to some lag & drift between versions; however, we expect that this will be OK, given that Bash itself is essentially feature-complete, so any newly-introduced ShellCheck warnings are not expected to be critical.

* The new template and this ADR will be announced on the forums and Slack.

* ShellCheck will continue to be used in `openedx-atlas <https://github.com/openedx/openedx-atlas>`_.

* The new ShellCheck template will be used to add checking to edx-platform PRs and master. Existing violations will be resolved or granted amnesty (that is: disabled with a cautionary comment).

* We will share this ADR with the Maintainership Pilot team, which has been compiling a tentative list of repository standards, so that they may consider ShellCheck as a standard check for applicable repositories.


Rejected Alternatives
*********************

* **Retroactive application:** We do not plan to retroactively apply ShellCheck to every repository with shell scripts. This would require resolving or applying amnesty to all existing violations, which does not seems worthwhile at this time.

* **Alternative linting tools:** We did not find any ShellCheck-like tools with comparable documentation, popularity, or ubiquity.

* **ShellCheck in the Python cookiecutters:** We could add the ShellCheck workflow to edx-cookiecutters so that it is run on PRs for all new repositories. However, most new repositories will not need shell scripts, so we do not plan on doing this.


Potential Future Work
*********************

* For shell script *testing*, `ShellSpec <https://github.com/shellspec/shellspec>`_ looks interesting, although it is not as obviously mature as ShellCheck. This ADR considers its adoption out of scope, but future ADRs may consider taking a position on ShellSpec adoption. Individual repositories are, of course, welcome to try and evaluate it.

* A repository health check could be added with logic along the lines of: *Does this repo have shell scripts? If so, does it run ShellCheck?*
