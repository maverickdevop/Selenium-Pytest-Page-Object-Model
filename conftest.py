import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

""" Create Global Fixture For Initialize Driver"""
@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    global driver

    if request.param == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        print("Set available driver")

    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield
    driver.quit()


""" Additional settings for driver """
""" Driver Options Full-HD for Google Chrome """
@pytest.fixture
def get_chrome_fullhd_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('-start-maximized')
    options.add_argument('--window-size=1920,1080')
    return options


""" Driver Options for 4K Google Chrome """
@pytest.fixture
def get_chrome_4k_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('-start-maximized')
    options.add_argument('--window-size=3840,2160')
    return options


""" Get Chrome driver with Full HD options """
@pytest.fixture
def get_webdriver_fullhd(get_chrome_fullhd_options):
    global driver

    options = get_chrome_fullhd_options
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


""" Get Chrome 4K resolution driver with options """
@pytest.fixture
def get_webdriver_4k(get_chrome_4k_options):
    global driver

    options = get_chrome_4k_options
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
