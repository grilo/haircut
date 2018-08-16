#!/usr/bin/env python

import logging
import os


class File(object):

    def __init__(self, name):
        self.props = {
            "name": name,
        }
        self.path = None
        self.template = ""

    def to_file(self):
        if not os.path.isfile(self.path):
            directory = os.path.dirname(self.path)
            if not os.path.isdir(directory):
                os.makedirs(directory)
            else:
                logging.warning("Content will be overwritten, directory already exists: %s", directory)

        for key, value in self.props.items():
            self.template = self.template.replace('{{ ' + key + ' }}', value)

        logging.info("Creating: %s", self.path)
        with open(self.path, 'w') as tpl_file:
            tpl_file.write(self.template)
