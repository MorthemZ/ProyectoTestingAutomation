from selenium.webdriver.common.by import By
#De Selenium que es es la librería principal de Python que sirve para automatizar navegadores, webdrive que es el módulo que controla los navegadores usa la herramientas que se usan en cualquier navegador de forma general usando el modulo by para usar la clase By para localizar elementos en la misma

import time
#Importa el modulo time de Python para trabajar con tiempos y pausas, Su uso más común en Selenium es time.sleep(segundos) para detener la ejecución del script por unos segundos, dando tiempo a que la página cargue antes de seguir.

def login(driver):
#def → palabra clave de Python que sirve para definir una función.
#login es el nombre de la funcion en este caso.
#driver es el parametro(Un parámetro es un valor que le pasás a una función para que pueda hacer su trabajo,es como la “materia prima” que la función necesita para producir un resultado,no es la función en sí, ni lo que hace, sino lo que le das para que funcione) que recibe la funcion.
    
    driver.get("https://www.saucedemo.com/")
#Toma el paramento driver(Es el parámetro que representa el navegador que Selenium controla.) con la accion get para tomar la url que le paso
    
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
#Toma el parametro driver con la accion de buscar el elemento user-name por su id y con send keys le escribe standard_user
#send_keys Es un método del objeto encontrado y simula escribir en ese campo exactamente como lo haría un humano con el teclado
    
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
#Lo mismo pero con password
    
    driver.find_element(By.ID,"login-button").click()
#Seria lo mismo que los casos anteriores pero en vez de simular escribir, hace la accion de hacer click
    
    time.sleep(2)
#En este caso me permite ver la pagina 2 segundos para ver si la pagina cargo todos los datos y logeo correctamente



#git add .
#git commit -m "Descripción de lo que cambió"
#git push


###CONFTEST###

#conftest es un archivo que usamos para hacer los fixture y se puede usar globalmente!

import pytest
#Framework de testing en Python. Permite crear tests automáticos y usar fixtures.

from selenium import webdriver
#En este caso no se pasa ni el common ni  el by porque no estamos buscando elementos solo estamos creando el navegador y pasandolo al test.

from utils import login
#De utils importamos la funcion login para  abrir la pagina y logear.

@pytest.fixture
#@pytest.fixture → decorador de Python que le dice a Pytest: “Esta función no es un test, es un recurso que puede usarse en tests”.
def driver():
    driver = webdriver.Chrome()
#Es para aclararle a funcion que use chrome como navegador y al ser una funcion puedo reutilizar driver.
    yield driver
#Entrega un recurso preparado por la fixture al test, ese recurso puede ser cualquier cosa que el test necesite: navegador, datos, archivos, etc.
    driver.quit()
#driver.quit() cierra el navegador completo que se abrió con webdriver.Chrome(), se ejecuta después del test, gracias al fixture con yield.


@pytest.fixture
#@pytest.fixture → decorador de Python que le dice a Pytest: “Esta función no es un test, es un recurso que puede usarse en tests”.
def login_in_driver(driver):
#Funcion que logea usando el fixture con la funcion driver para abrir chrome como parametro y usa la funcion de logeo de utils.py usando como paramentro el fixture anterior nuevamente
    login(driver)
#Función que hace el login automáticamente.
    return driver
#Entrega el navegador logueado al test.


#ASSERT:
# El assert en Python es una instrucción para verificar que algo sea verdadero. Si la condición es falsa, Python lanza un AssertionError, que en Pytest marca el test como fallido. POR EJ:
#   def test_login_validation(login_in_driver):
#            driver = login_in_driver
#>           assert "/inventori.html" in driver.current_url, "No se redirigio al inventario"
#E           AssertionError: No se redirigio al inventario
#E           assert '/inventori.html' in 'https://www.saucedemo.com/inventory.html'
#E            +  where 'https://www.saucedemo.com/inventory.html' = <selenium.webdriver.chrome.webdriver.WebDriver (session="d01683d243ad45149800f900a456cfec")>.current_url

#tests\test_login.py:6: AssertionError


def test_inventory(login_in_driver):
        driver = login_in_driver
        
        assert driver.title == "Swag Labs"
#Verifica que el titulo de la pagina sea Swag Labs
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
#En la variable products guarda la info de los elementos inventory_item que encuentre por el class name
#find_elements (con “s”) devuelve una lista de elementos, aunque no haya ninguno. En cambio, find_element (sin “s”) devuelve solo el primero y lanza error si no encuentra nada
#Siempre que busques varios elementos, usá find_elements y combiná con assert para decidir cuándo el test debe fallar. Esto hace que tu test sea más predecible y legible.
        assert len(products) > 0, "No hay productos visibles en la pagina"