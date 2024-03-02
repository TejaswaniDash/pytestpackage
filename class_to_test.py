"""
Structure Tests in a Test Class

* How to use test class to wrap methods under one class
* How to use a, actually test a class, a real program
* Autouse Keyword in fixtures
* Assert the result to create a real test scenario

 py.test -s -v pytestpackage/test_class_demo.py --browser firefox
"""

class SomeClassToTest():

    def __init__(self, value):
        #constructor
        self.value = value
        # take value from constructor

    def sumNumbers(selfself, a, b):
        return a + b + self.value

