from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    #Navegar a la página de login de saucedemo.com
    driver.get("https://www.saucedemo.com/")

    #Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()

    #Login automatizado con espera explícita
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))