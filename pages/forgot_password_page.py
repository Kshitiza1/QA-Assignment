from locators.login_locators import LoginLocators
from selenium.webdriver.support import expected_conditions as EC


class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = driver.wait

    def click_reset_password_btn(self):
        self.wait.until(EC.element_to_be_clickable(LoginLocators.reset_password_btn)).click()

    def page_should_contain(self, text):
        message_text = self.wait.until(EC.visibility_of_element_located(LoginLocators.msg_container)).text
        assert text in message_text, f"Expected text '{text}' not found on page!"
