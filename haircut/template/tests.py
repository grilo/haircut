#!/usr/bin/env python

import os

import haircut.template.base


template = """#!/usr/bin/env python

import sys
import pytest

import {{ name }}.cli

def test_main(monkeypatch):
    testargs = ["-v"]
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', testargs)
        assert {{ name }}.cli.main() == True

"""

class File(haircut.template.base.File):

    def __init__(self, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)
        self.path = os.path.join(self.props["name"], 'tests', 'test_cli.py')
        self.template = template
