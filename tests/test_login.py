from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_validation(login_in_driver):
        driver = login_in_driver
#Validar login exitoso verificando que se haya redirigido a la página de inventario
        assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"
#Validación de “Products/Swag Labs”.
        titulo = driver.find_element(By.CLASS_NAME, "title").text
        assert titulo == "Products", f"Título incorrecto: se esperaba 'Products' y se obtuvo '{titulo}'"
#Validación de “Products/Swag Labs”.
        logo_title = driver.find_element(By.CLASS_NAME,"app_logo").text
        assert logo_title == "Swag Labs", f"Título Logo incorrecto: se esperaba 'Swag Labs' y se obtuvo '{logo_title}'"