import pytest

""" Use This Class For All Test With Fixture Driver """


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
