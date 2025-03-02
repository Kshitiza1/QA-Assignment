import pytest

from pages.login_page import LoginPage


class TestLogin:
    def test_valid_login(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login_button()
        assert "dashboard" in driver.current_url.lower(), "Login failed!"

    def test_invalid_username_valid_password(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.enter_username("User")
        login_page.enter_password("admin123")
        login_page.click_login_button()
        login_page.get_invalid_credential_message()
        assert "Invalid credentials" in login_page.get_invalid_credential_message(), "Error message not displayed!"

    def test_valid_username_invalid_password(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("user123")
        login_page.click_login_button()
        login_page.get_invalid_credential_message()
        assert "Invalid credentials" in login_page.get_invalid_credential_message(), "Error message not displayed!"

    def test_invalid_login(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.enter_username("User")
        login_page.enter_password("user123")
        login_page.click_login_button()
        login_page.get_invalid_credential_message()
        assert "Invalid credentials" in login_page.get_invalid_credential_message(), "Error message not displayed!"

    @pytest.mark.task2
    def test_empty_fields(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.click_login_button()
        username_req, password_req = login_page.get_required_messages()
        assert "Required" in username_req, "Username required is not displayed!"
        assert "Required" in password_req, "Password required is not displayed!"

    def test_password_masking(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.is_password_masked()
        assert login_page.is_password_masked(), "Password is not masked!"
