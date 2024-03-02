"""
* how we can provide arguments from the command line to our test cases.
* Assume a scenario where you are testing a website on different browsers, maybe you want to run your test once
  on Firefox, second time you want to run your test on Chrome.
  And you want to say from the command line, this time run my test on Firefox, the other time run my test on Chrome.

py.test -s -v pytestpackage/test_command_line_args.py--browser firefox
py.test -s -v pytestpackage/test_command_line_args.py--browser chrome
"""

import pytest


def test_command_line_methodA( oneTimeSetUp , setUp):
    print("Running method A")


def test_command_line_methodB( oneTimeSetUp , setUp):
    print("Running method B")