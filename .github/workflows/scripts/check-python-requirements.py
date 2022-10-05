#!/usr/bin/env python3
# Requires 'click'

import click
import os
import sys
from collections import namedtuple
from dataclasses import dataclass


@dataclass
class Issue:
    path: str
    line_number: int
    line_text: str
    message: str


@click.command(help="Check that a repository's Python requirements follow OEP-18")
@click.option("--requirements-path", type=str, default="./requirements")
@click.option("--allow-url-requirements/--forbid-url-requirements", default=False)
@click.option("--allow-direct-constraints/--forbid-direct-constraint", default=False)
def main(requirements_path, allow_url_requirements, allow_direct_constraints):

    req_file_paths = []  # ".in" files should hold version-agnostic requirements
    pin_file_paths = []  # ".txt" files should hold specific pins of requirements

    for dir_entry in os.scandir(requirements_path):
        if not dir_entry.is_file:
            continue
        if dir_entry.name == "constraints.txt":
            # unlike other .txt files, constraints.txt holds version
            # constraints, *not* version pins.
            continue
        if dir_entry.name.endswith(".txt"):
            pin_file_paths.append(dir_entry.path)
        if dir_entry.name.endswith(".in"):
            req_file_paths.append(dir_entry.path)

    warnings = []
    errors = []

    for req_file_path in req_file_paths:
        with open(req_file_path) as req_file:
            for line_number, raw_line in enumerate(req_file):
                line = raw_line.split("#")[0].strip()
                if not line:
                    continue
                if "http://" in line or "https://" in line:
                    issue = Issue(
                        path=req_file_path,
                        line_number=line_number,
                        line_text=line,
                        message=(
                            "OEP-18 forbids URL-based Python dependencies. "
                            "Please publish this package to PyPI and "
                            "install it as a standard requirement."
                        )
                    )
                    if allow_url_requirements:
                        warnings.append(issue)
                    else:
                        errors.append(issue)
                if "=" in line or "<" in line or ">" in line:
                    issue = Issue(
                        path=req_file_path,
                        line_number=line_number,
                        line_text=line,
                        message=(
                            "OEP-18 requires that Python package version constraints "
                            "be put in constraints.txt, not the *.in files."
                        ),
                    )
                    if allow_direct_constraints:
                        warnings.append(issue)
                    else:
                        errors.append(issue)
                if line.startswith("-r ") and line.endswith(".txt") and line != "-r constraints.txt":
                    issue = Issue(
                        path=req_file_path,
                        line_number=line_number,
                        line_text=line,
                        message=(
                            "Per OEP-18, *.in files can include other *.in files as well as "
                            "constraints.txt. They sould _not_ include other *.txt files."
                        ),
                    )
                    errors.append(issue)

    print("TODO: check pin files")

    print("TODO - better output formatting")
    print("WARNINGS", *warnings, sep="\n")
    print("ERRORS", *errors, sep="\n")
    if errors:
        raise sys.exit(1)

if __name__ == "__main__":
    main()

