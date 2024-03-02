"""
* Here we are using couple of fixtures, oneTimeSetUp and setUp.
* This is coming from our conftest file, which has a setUp,
# this is a function level because we didn't provide anything.
# And this is the oneTimeSetUp

* command to use in terminal to run the test-
py.test -v -s pytestpackage/test_run_order_demo.py

* for ordering specific run-
https://pytest-ordering.readthedoocs.io/en/develop/
"""

import pytest

#def test_run_order_methodA( oneTimeSetUp , setUp):
#    print("Running method A")

#def test_run_order_methodB( oneTimeSetUp , setUp):
#    print("Running method B")

#def test_run_order_methodC( oneTimeSetUp , setUp):
#    print("Running method C")

#def test_run_order_methodD( oneTimeSetUp , setUp):
#    print("Running method D")

#def test_run_order_methodE( oneTimeSetUp , setUp):
#    print("Running method E")

#def test_run_order_methodF( oneTimeSetUp , setUp):
#    print("Running method F")

"""
To do it in specific order 
"""
# Desired order= B, A , C, E, D, F
@pytest.mark.run(order=2)
def test_run_order_methodA( oneTimeSetUp , setUp):
    print("Running method A")

@pytest.mark.run(order=1)
def test_run_order_methodB( oneTimeSetUp , setUp):
    print("Running method B")

@pytest.mark.run(order=3)
def test_run_order_methodC( oneTimeSetUp , setUp):
    print("Running method C")

@pytest.mark.run(order=5)
def test_run_order_methodD( oneTimeSetUp , setUp):
    print("Running method D")

@pytest.mark.run(order=4)
def test_run_order_methodE( oneTimeSetUp , setUp):
    print("Running method E")

@pytest.mark.run(order=6)
def test_run_order_methodF( oneTimeSetUp , setUp):
    print("Running method F")
