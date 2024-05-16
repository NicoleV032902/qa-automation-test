import pytest

# putting all the fixtures in 1 file. this is where the parent class will be stored. All the child class that will be
# executed in the next file will inherit this parents once it is called and don't need to define @pytest-- redundantly


@pytest.mark.usefixtures("setting_browser")
class SetupBrowser:
    pass


# @pytest.mark.userfixtures("Admin_Login")
# class AdminLogin:
#     pass
#
#
# @pytest.mark.userfixtures("DealerAdmin_Login")
# class DealerAdminLogin:
#     pass
#
#
# @pytest.mark.userfixtures("Dealer_Login")
# class DealerLogin:
#     pass
