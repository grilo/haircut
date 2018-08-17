#!/usr/bin/env python

import os

import haircut.template.base


template = """pytest --cov={{ name }} --cov-report term-missing -s -vv\n"""

class File(haircut.template.base.File):

    def __init__(self, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)
        self.path = os.path.join(self.props["name"], 'coverage.sh')
        self.template = template
