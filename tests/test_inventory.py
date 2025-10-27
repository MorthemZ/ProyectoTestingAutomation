from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_inventory(login_in_driver):
        driver = login_in_driver
#Verificar que el título(etiqueta html) de la página de inventario sea correcto
        assert driver.title == "Swag Labs"

#Espera explícita antes de buscar los productos, para asegurar de que la página terminó de cargar.
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
#Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)        
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No hay productos visibles en la pagina"
#Lista nombre/precio del primero
#Tomo el primer producto de la lista
        primer_producto = products[0]
#Obtiene el elemento que contiene su nombre y su precio usando products para que busque la lista de los mismos y primer producto para que agarre el del primero
        nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
        print("Primer producto: " + nombre + " y Precio primer producto:" + precio)

#Validar que elementos importantes de la interfaz estén presentes menú
        boton_menu_ham = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
        assert  boton_menu_ham.is_displayed(), "El menu hamburguesa no está visible"
#Validar que elementos importantes de la interfaz estén presentes filtros
        selector_filtro = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container")))
        assert selector_filtro.is_displayed(), "El selector del filtro no es visible"