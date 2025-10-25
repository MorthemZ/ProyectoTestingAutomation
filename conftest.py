import pytest
from selenium import webdriver
from utils import login
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_opt = Options()
    #abre chrome como incognito y desactiva popup de
    #contraseña filtrada, que impedia que los test cases se ejecuten bien
    chrome_opt.add_argument("--incognito")
     # Maximizar ventana al abrir
    chrome_opt.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_opt)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver
