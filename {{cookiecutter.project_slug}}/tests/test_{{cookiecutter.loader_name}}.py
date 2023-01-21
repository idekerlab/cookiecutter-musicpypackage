#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.project_slug }}` package."""

import os
import tempfile
import shutil
{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else %}
import unittest
{%- endif %}
from {{ cookiecutter.project_slug }} import {{ cookiecutter.loader_name }}
{%- if cookiecutter.use_pytest == 'y' %}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
{%- else %}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_parse_arguments(self):
        """Tests parse arguments"""
        res = {{ cookiecutter.loader_name }}._parse_arguments('hi', [])

        self.assertEqual(res.profile, '{{ cookiecutter.project_slug }}')
        self.assertEqual(res.verbose, 0)
        self.assertEqual(res.logconf, None)
        self.assertEqual(res.conf, None)

        someargs = ['-vv', '--logconf', 'hi']
        res = {{cookiecutter.loader_name}}._parse_arguments('hi', someargs)

        self.assertEqual(res.verbose, 2)
        self.assertEqual(res.logconf, 'hi')


    def test_setup_logging(self):
        """ Tests logging setup"""
        try:
            {{cookiecutter.loader_name}}._setup_logging(None)
            self.fail('Expected AttributeError')
        except AttributeError:
            pass

        # args.logconf is None
        res = {{cookiecutter.loader_name}}._parse_arguments('hi', [])
        {{cookiecutter.loader_name}}._setup_logging(res)

        # args.logconf set to a file
        try:
            temp_dir = tempfile.mkdtemp()

            logfile = os.path.join(temp_dir, 'log.conf')
            with open(logfile, 'w') as f:
                f.write("""[loggers]
keys=root

[handlers]
keys=stream_handler

[formatters]
keys=formatter

[logger_root]
level=DEBUG
handlers=stream_handler

[handler_stream_handler]
class=StreamHandler
level=DEBUG
formatter=formatter
args=(sys.stderr,)

[formatter_formatter]
format=%(asctime)s %(name)-12s %(levelname)-8s %(message)s""")

            res = {{cookiecutter.loader_name}}._parse_arguments('hi', ['--logconf',
                                                                       logfile])
            {{cookiecutter.loader_name}}._setup_logging(res)

        finally:
            shutil.rmtree(temp_dir)

    def test_main(self):
        """Tests main function"""

        # try where loading config is successful
        try:
            temp_dir = tempfile.mkdtemp()
            res = {{cookiecutter.loader_name}}.main(['myprog.py'])
            self.assertEqual(res, 0)
        finally:
            shutil.rmtree(temp_dir)

{%- endif %}
