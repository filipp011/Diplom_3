import allure
from pages.password_recovery_page import PasswordRecoveryPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestResetPassword:
    @allure.title("Проверяем, что пароль можно восстановить")
    def test_password_resset(self, driver):
        # Arrange
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page = MainPage(driver)
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_to_recovery_password_link()

        # Act
        password_recovery_page.enter_email_to_recovery_password()
        expected_result = "Пароль"

        # Assert
        assert password_recovery_page.check_password_recovery_field() == expected_result

    @allure.title("Проверяем видимость пароля")
    def test_password_is_visible(self, driver):
        # Arrange
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page = MainPage(driver)
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_to_recovery_password_link()

        # Act
        password_recovery_page.enter_email_to_recovery_password()
        password_recovery_page.enter_new_password()
        password_recovery_page.click_password_make_visible_hidden()

        # Assert
        assert password_recovery_page.check_password_visible()

    @allure.title("Проверяем, что вводимый пароль скрывается")
    def test_password_is_hidden(self, driver):
        # Arrange
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page = MainPage(driver)
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_to_recovery_password_link()

        # Act
        password_recovery_page.enter_email_to_recovery_password()
        password_recovery_page.enter_new_password()
        password_recovery_page.click_password_make_visible_hidden()
        password_recovery_page.click_password_make_visible_hidden()

        # Assert
        assert password_recovery_page.check_password_hidden()
