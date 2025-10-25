from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver

        assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"

    except Exception as e:
        print(f"Error en  test_login: {e}")
        raise
    finally:
        driver.quit()



#💡 Ejemplo completo de flujo

#Supongamos que cambiaste test_login.py y agregaste un nuevo test:

#git status
#git add .
#git commit -m "Agrego nuevo test para validar inventario"
#git push


#Listo 🚀
#Cuando entres a tu repo en GitHub, vas a ver los cambios aplicados.

# Si querés actualizar tu repo local (por si editás desde GitHub también)
#git pull


#Eso trae los cambios del remoto hacia tu PC.