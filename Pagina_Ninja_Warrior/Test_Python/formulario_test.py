import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from formulario import Formulario
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://127.0.0.1:5500/Pagina_Ninja_Warrior/formulario.html")
    yield driver
    driver.quit()

def test_envio_exitoso(driver):
    formulario = Formulario(driver)
    formulario.submit_form("Carlos", "Valencia", "26", "carlos@gmail.com", "Este es un mensaje de prueba")
    
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.accept()
    
    assert driver.find_element(By.ID, "nombre").get_attribute("value") == ""

def test_errores_validacion(driver):
    formulario = Formulario(driver)
    formulario.submit_form("J", "P", "-5", "carlosejemplo.com", "Corto")
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message")))
    
    error_messages = formulario.get_error_messages()
    assert len(error_messages) > 0
    
    expected_errors = [
        "El nombre debe tener al menos 3 caracteres.",
        "Apellido inválido",
        "Edad inválida",
        "Correo electrónico inválido",
        "El mensaje debe contener al menos 10 caracteres."
    ]
    actual_errors = [error.text for error in error_messages]
    
    for expected in expected_errors:
        assert expected in actual_errors