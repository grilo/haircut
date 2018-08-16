#!/usr/bin/env python

import os

import haircut.template.base


class File(haircut.template.base.File):

    def __init__(self, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)
        self.path = os.path.join(self.props["name"], 'confest.py')
