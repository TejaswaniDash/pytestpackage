"""
* how we can generate the Test Report
* how we can generate the HTML report
 in terminal-  py.test -s -v pytestpackage/test_class_demo2.py --browser firefox --html = ( path of the location)
# '--html', that's it, '=', the name of the file, or you can provide the full path where you want the file.

* Example-  in terminal-  py.test -s -v pytestpackage/test_class_demo2.py --browser firefox --html=htmlrepot.html

"""

import pytest
from pytestpackage.class_to_test import SomeClassToTest



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestRepotingDemo():
    @pytest.fixture(autouse = True)


    def classSetUp(self, oneTimeSetUp):
        self.abc = SomeClassToTest(self.value)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result== 20
         print("Running method A")

    def test_methodB():
        result = self.abc.sumNumbers(2, 8)
        assert result > 20
         print("Running method B")