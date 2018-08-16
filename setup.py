#!/usr/bin/env python

from distutils.core import setup

setup(name='haircut',
      version='0.1',
      description='Python project scaffolding',
      author='Joao Grilo',
      author_email='joao.grilo@gmail.com',
      url='https://github.com/grilo/haircut',

      entry_points={
        'console_scripts': [
            'haircut = haircut.cli:main',
        ],
      }
    )
