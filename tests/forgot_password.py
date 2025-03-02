from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


class TestForgotPassword:
    def test_forgot_password(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        login_page.click_forgot_password()
        login_page.enter_username("Admin")
        forgot_password_page.click_reset_password_btn()
        assert "sendPasswordReset" in driver.current_url, "Reset Password Unsuccessful"
        forgot_password_page.page_should_contain("Reset Password link sent successfully")

