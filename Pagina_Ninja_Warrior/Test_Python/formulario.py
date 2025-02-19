from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Formulario:
    def __init__(self, driver):
        self.driver = driver
        self.nombre_field = (By.ID, 'nombre')
        self.apellidos_field = (By.ID, 'apellidos')
        self.edad_field = (By.ID, 'edad')
        self.email_field = (By.ID, 'email')
        self.mensaje_field = (By.ID, 'mensaje')
        self.submit_button = (By.CSS_SELECTOR, 'input[type="submit"]')
        self.error_messages = (By.CSS_SELECTOR, '.error-message')

    def wait_for_element(self, by_locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(by_locator))

    def submit_form(self, nombre, apellidos, edad, email, mensaje):
        self.wait_for_element(self.nombre_field).send_keys(nombre)
        self.wait_for_element(self.apellidos_field).send_keys(apellidos)
        self.wait_for_element(self.edad_field).send_keys(edad)
        self.wait_for_element(self.email_field).send_keys(email)
        self.wait_for_element(self.mensaje_field).send_keys(mensaje)
        self.wait_for_element(self.submit_button).click()

    def get_error_messages(self):
        return self.driver.find_elements(*self.error_messages)