from selenium.webdriver.common.by import By


class LoginLocators:
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[@type='submit']")
    invalid_credential_error_msg = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
    username_required_error_msg = (By.XPATH, "(//span[contains(@class, 'oxd-input-field-error-message')])[1]")
    password_required_error_msg = (By.XPATH, "(//span[contains(@class, 'oxd-input-field-error-message')])[2]")
    forgot_password = (By.CLASS_NAME, "orangehrm-login-forgot")
    reset_password_btn = (By.XPATH, "(//button[contains( @class,'orangehrm-forgot-password-button--reset')])")
    msg_container = (By.CLASS_NAME, "orangehrm-card-container")
    user_dropdown_tab = (By.CLASS_NAME, "oxd-userdropdown-tab")
    logout = (By.XPATH, "//ul[@class='oxd-dropdown-menu']//a[@href='/web/index.php/auth/logout']")
