from pages.login_page import LoginPage


class TestLogout:
    def test_logout_functionality(self, setup, login):
        driver = setup
        login_page = LoginPage(driver)
        login_page.click_user_dropdown_tab()
        login_page.click_logout()
        assert "login" in driver.current_url.lower(), "Logout failed!"
