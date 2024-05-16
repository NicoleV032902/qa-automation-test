import pytest
from utilities import baseClasses


@pytest.mark.usefixtures("setting_browser")
def testFunction():
    print("Pass")
