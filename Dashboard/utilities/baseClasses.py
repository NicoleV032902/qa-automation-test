import pytest


@pytest.mark.userfixtures("setting_browser")
class SetupBrowser:
    pass


@pytest.mark.userfixtures("Admin_Login")
class AdminLogin:
    pass


@pytest.mark.userfixtures("DealerAdmin_Login")
class DealerAdminLogin:
    pass


@pytest.mark.userfixtures("Dealer_Login")
class DealerLogin:
    pass
