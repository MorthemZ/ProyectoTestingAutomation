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



