#!/usr/bin/env python

import os

import haircut.template.base


template = """ #!/usr/bin/env python

from distutils.core import setup

setup(name='{{ name }}',
      version='0.1',
      description='Autogenerated python project.',
      author='The Author',
      author_email='author@mail.com',
      url='https://url/for/{{ name }}',

      entry_points={
        'console_scripts': [
            '{{ name }} = {{ name }}.cli:main',
        ],
      }
    )
"""


class File(haircut.template.base.File):

    def __init__(self, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)
        self.path = os.path.join(self.props["name"], 'setup.py')
        self.template = template
