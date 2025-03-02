from locators.login_locators import LoginLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = driver.wait

    def enter_username(self, username):
        self.wait.until(EC.presence_of_element_located(LoginLocators.username)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located(LoginLocators.password)).send_keys(password)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(LoginLocators.login_btn)).click()

    def get_invalid_credential_message(self):
        return self.wait.until(EC.visibility_of_element_located(LoginLocators.invalid_credential_error_msg)).text

    def get_required_messages(self):
        username_required = self.wait.until(EC.visibility_of_element_located(LoginLocators.username_required_error_msg)).text
        password_required = self.wait.until(EC.visibility_of_element_located(LoginLocators.password_required_error_msg)).text
        return username_required, password_required

    def is_password_masked(self):
        password_field = self.wait.until(EC.presence_of_element_located(LoginLocators.password))
        return password_field.get_attribute("type") == "password"

    def click_forgot_password(self):
        self.wait.until(EC.visibility_of_element_located(LoginLocators.forgot_password)).click()

    def click_user_dropdown_tab(self):
        self.wait.until(EC.visibility_of_element_located(LoginLocators.user_dropdown_tab)).click()

    def click_logout(self):
        self.wait.until(EC.visibility_of_element_located(LoginLocators.logout)).click()