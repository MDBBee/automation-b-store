import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print("Launching chrome browser.........")
        return webdriver.Chrome()
    elif browser == 'firefox':
        print("Launching firefox browser.........")
        return webdriver.Firefox()
    else:
        return webdriver.Edge()


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# PyTest HTML Report
# It is hook for Adding Environment info to HTML Report
def pytest_metadata(metadata):
    metadata['Project Name'] = 'B-Store'
    metadata['Module Name'] = 'Customers'
    metadata['Tester'] = 'Bobby'

    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
