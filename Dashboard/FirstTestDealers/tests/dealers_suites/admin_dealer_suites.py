from lib2to3.pgen2 import driver
import pytest
from selenium.webdriver.common.by import By

from utilities.baseClasses import AdminLogin, DealerAdminLogin


class TestAdminDealersFlow(AdminLogin):
    def test_Admin_Dealers_Flow(self):
        pass


class TestDealerAdminDealersFlow(DealerAdminLogin):
    def test_Dealer_Admin_Dealers_Flow(self):
        pass
