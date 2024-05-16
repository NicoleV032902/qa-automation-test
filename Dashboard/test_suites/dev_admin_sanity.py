import pytest
from utilities.baseClasses import BaseClasses


# @pytest.mark.userfixtures("setting_browser")
class LoginTest(BaseClasses):
    def login_example(self):
        print("scrip start from here")
