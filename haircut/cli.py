#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Some description."""

import logging
import argparse
import sys

import haircut.project


def main():

    if sys.version_info < (2,6) or sys.version_info > (2,8):
        raise SystemExit('Sorry, this code needs Python 2.6 or Python 2.7 (current: %s.%s)' % (sys.version_info[0], sys.version_info[1]))

    desc = "Generate the scaffold for a basic python project."
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument("-p", "--project", required=True,
                        help="The name of the project directory.")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Increase output verbosity")

    args = parser.parse_args()

    logging.basicConfig(format='%(asctime)s::%(levelname)s::%(module)s::%(message)s')
    logging.getLogger().setLevel(getattr(logging, 'INFO'))

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    return haircut.project.Base(args.project).generate()
