import allure

import urls
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestAccountPage:
    @allure.title("Проверка входа в личный кабинет")
    def test_account_click_on_button(self, driver, create_new_user_and_delete):
        # Arrange
        main_page = MainPage(driver)
        main_page.click_account_button()
        email, password, _ = create_new_user_and_delete

        # Act
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_modal_for_ff()
        main_page.click_account_button()

        # Assert
        expected_result = "Выход"
        assert account_page.check_logout_button() == expected_result

    @allure.title("Проверяем переход в раздел история заказов")
    def test_click_history_order(self, driver, create_new_user_and_delete):
        # Arrange
        main_page = MainPage(driver)
        main_page.click_account_button()
        email, password, _ = create_new_user_and_delete

        # Act
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_modal_for_ff()
        main_page.click_account_button()
        account_page.get_order_history()

        # Assert
        expected_result = urls.ORDER_HISTORY_URL
        assert account_page.check_order_history_url() == expected_result

    @allure.title("Провереям выход из акка")
    def test_logout(self, driver, create_new_user_and_delete):
        # Arrange
        main_page = MainPage(driver)
        main_page.click_account_button()
        email, password, _ = create_new_user_and_delete

        # Act
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_modal_for_ff()
        main_page.click_account_button()
        account_page.logout_from_account()

        # Assert
        expected_result = "Войти"
        assert login_page.get_login_button_from_login_page() == expected_result
