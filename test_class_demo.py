"""
Structure Tests in a Test Class
"""

import pytest
from pytestpackage.class_to_test import SomeClassToTest


# Imagine we have 20 methods or maybe 100 methods
# in that case we will put the fixtures on top of the class

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():
    @pytest.fixture(autouse = True)

   # we will use the 'autouse' keyword, and It's say "True"
#What it does is?
    # it creates the fixture,
    # it makes the fixture available to the complete scope where it's present,
    # and any other place will be able to use that fixture, so anywhere else

    def classSetUp(self):
        self.abc = SomeClassToTest(10)
        # how do these test methods they know that there is a self.abc instance created


    # We will create one more fixture in our test class
# The purpose of fixture is to create some kind of objects or instances,
# or to prepare some other data, which is going to help us in running our test method.

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result== 20
         print("Running method A")

    def test_methodB():
         print("Running method B")
