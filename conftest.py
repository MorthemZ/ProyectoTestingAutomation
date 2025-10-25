import pytest
from selenium import webdriver
from utils import login

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver

#conftest es un archivo que usamos para hacer los fixture y se puede usar globalmente!