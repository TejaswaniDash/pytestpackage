
import pytest
#create a setUp method
@pytest.yield_fixture()
# yield_fixture() allows us to run the same method before and after, a
def setUp():
    print("once before every method")
    yield
    print("once after every method")

def test_demo2_methodA(setUp):
    #pass the name of the fixture in the method
    print("Running method A")

def test_demo2_methodB(setUp):
    print("Running method B")