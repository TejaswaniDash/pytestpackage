"""
PYTHON pytest.fixture()

pytest we can run in terminal/console
"""


import pytest
#create a setUp method
@pytest.fixture()
def setUp():
    print("once before every method")

def test_demo1_methodA(setUp):
    #pass the name of the fixture in the method
    print("Running method A")

def test_demo1_methodB(setUp):
    print("Running method B")

