#!/usr/bin/env python

import os

from template import setup, cli, readme, tests, conftest, init, gitignore, requirements_dev, coverage


class Base(object):

    def __init__(self, name):
        self.name = name
        self.templates = [
            setup.File(name),
            cli.File(name),
            readme.File(name),
            tests.File(name),
            conftest.File(name),
            init.File(name),
            gitignore.File(name),
            requirements_dev.File(name),
            coverage.File(name),
        ]

    def generate(self):
        for template in self.templates:
            template.to_file()
