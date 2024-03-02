"""
It will contatin all the common fixtures that we are gonna use for multiple modules

"""

import pytest

@pytest.yield_fixture()
# yield_fixture() allows us to run the same method before and after, a
def setUp():
    print("Running conftest demo method setUp")
    yield
    print("Running conftest demo method teardown")


"""
Here in below I want to have a setUp which runs only once before the module starts, 
and then let it finish all the tests under the module, and then finally when all the 
tests are completed, run the tearDown.
"""

@pytest.yield_fixture(scope="module")
#def oneTimeSetUp():

#    print("Running conftest demo one time setUp")
#    yield
#   print("Running conftest demo one time teardown")

# How do we make it look different?
# inside of the fixture we can define the scope
# scope= "module", that is going to apply to the complete module,
# which means it runs once before the module, once after the module

# @pytest.yield_fixture(scope="module")
# def oneTimeSetUp(browser, osType):
#    print("Running one time setUp")
#    if browser == 'firefox':
#        print("Running test on FF")
#    else:
#        print("Running test on Chrome")
#    yield
#    print("Running one time teardown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    if browser == 'firefox':
        value = 10
        print("Running test on FF")
    else:
        value = 20
        print("Running test on Chrome")

    if request.cls is not None
        request.cls.value = value
    yield value
    print("Running one time teardown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--ostype" , help="Type of operating system")

# adding option for the parser, whatever options we want to provide from the command line.
# whatever value provided in front of "--browser", that should be the browser's value.
# We can have a platform as well.
@pytest.fixture(scope= "session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope= "session")
def osType(request):
    return request.config.getoption("--osType")

# we created two fixtures, both run per session, the scope is "session", and the name is "--browser", and "--osType".


##let's put in our oneTimeSetUp kind of thing, this method.
# So what we can do is, this is a oneTimeSetUp,
# here we can set our test to run on either Firefox or either on Chrome.
