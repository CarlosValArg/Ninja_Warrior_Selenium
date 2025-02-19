from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from formulario import Formulario
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:5500/Pagina_Ninja_Warrior/formulario.html")

formulario = Formulario(driver)

formulario.submit_form("Carlos", "Valencia", "26", "carlos@gmail.com", "Este es un mensaje de prueba")

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

alert.accept()

time.sleep(2)

try:
    assert "Formulario enviado correctamente" in driver.page_source
    print("Test de éxito: El formulario fue enviado correctamente.")
except AssertionError:
    print("Test de fallo: El formulario no se envió correctamente.")

formulario.submit_form("J", "P", "-5", "carlosejemplo.com", "Corto")

formulario.wait_for_element((By.CSS_SELECTOR, ".error-message"))

error_messages = formulario.get_error_messages()
for error in error_messages:
    print(f"Error encontrado: {error.text}")

driver.quit()