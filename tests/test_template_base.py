#!/usr/bin/env python

import os

import pytest

import haircut.template.base


@pytest.yield_fixture(autouse=True)
def tmpdir():
    temp_dir = tempfile.mkdtemp(prefix='testpostdeploy')
    yield temp_dir
    shutil.rmtree(temp_dir)


def test_replace_props(tmpdir):
    os.chdir(tmpdir)
    base = haircut.template.base.File('hello')
    base.template("Something {{ world }}")
    #base.props = 
