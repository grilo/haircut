#!/usr/bin/env python

import os

import haircut.template.base


template = """
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import argparse


def main():

    desc = "Some description."
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Increase output verbosity")

    args = parser.parse_args()

    logging.basicConfig(format='%(asctime)s::%(levelname)s::%(module)s::%(message)s')
    logging.getLogger().setLevel(getattr(logging, 'INFO'))

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    return True
"""


class File(haircut.template.base.File):

    def __init__(self, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)
        self.template = template
        self.path = os.path.join(self.props["name"], self.props["name"], 'cli.py')
