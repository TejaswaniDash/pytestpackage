"""
How to Return a Value from Fixtures

Problem Statement:

let's imagine that when I have firefox, I want to provide some other value;
and if I have chrome, I want to provide some other value.
So the class, when we instantiated it, it accepts a value.
Let's imagine the problem statement is, I want to take this value based on the
condition of the parameter provided. So if I'm running my test with Firefox browser,
I want to provide some other value to this instance, if I am running my test with the Chrome browser,
I want to provide some other value to this instance,

 py.test -s -v pytestpackage/test_class_demo2.py --browser firefox

"""
import pytest
from pytestpackage.class_to_test import SomeClassToTest



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():
    @pytest.fixture(autouse = True)


    def classSetUp(self, oneTimeSetUp):
        self.abc = SomeClassToTest(self.value)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result== 20
         print("Running method A")

    def test_methodB():
         print("Running method B")
