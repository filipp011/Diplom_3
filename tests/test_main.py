import allure

from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage


class TestMainPage:
    @allure.title("Переход в раздел конструктора")
    def test_click_constructor_burger(self, driver, create_new_user_and_delete):
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
        main_page.click_constructor_link()

        # Assert
        expected_result = "Соберите бургер"
        assert main_page.check_constructor_title() == expected_result

    @allure.title("Переход в ленту заказов")
    def test_click_feed_orders(self, driver, create_new_user_and_delete):
        # Arrange
        email, password, _ = create_new_user_and_delete
        main_page = MainPage(driver)
        main_page.click_login_button()

        # Act
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        account_page = AccountPage(driver)
        account_page.close_modal_for_ff()
        main_page.get_feed()
        order_feed_page = OrderFeedPage(driver)

        # Assert
        expected_result = "Лента заказов"
        assert order_feed_page.check_feed_title_text() == expected_result

    @allure.title("Проверяем открытие модального окна ингридента")
    def test_ingredient_info_modal_window(self, driver):
        # Arrange
        main_page = MainPage(driver)

        # Act
        main_page.get_ingredient_details()

        # Assert
        expected_result = "Детали ингредиента"
        assert main_page.check_ingredient_title_text() == expected_result

    @allure.title("Проверка закрытия модального окна с информацией об ингредиенте")
    def test_ingredient_details_modal_window_closed(self, driver):
        # Arrange
        main_page = MainPage(driver)

        # Act
        main_page.get_ingredient_details()
        main_page.close_ingredient_details_modal()

        # Assert
        expected_result = "Соусы"
        assert main_page.check_ingredient_details_modal_closed() == expected_result

    @allure.title("Проверяем кол-во ингридентов после увеленичения")
    def test_add_ingredient_to_basket(self, driver):
        # Arrange
        main_page = MainPage(driver)
        before_ingredient_added = main_page.check_count_before_ingredient_added()

        # Act
        main_page.add_ingredient()
        after_ingredient_added = main_page.check_count_after_ingredient_added()

        # Assert
        assert int(after_ingredient_added) > int(before_ingredient_added)

    @allure.title("Проверяем можно ли сделать заказ после авторизации")
    def test_make_order_after_authorized(self, driver, create_new_user_and_delete):
        # Arrange
        email, password, _ = create_new_user_and_delete
        main_page = MainPage(driver)
        main_page.click_login_button()

        # Act
        login_page = LoginPage(driver)
        login_page.user_login(email, password)
        main_page.make_order()

        # Assert
        expected_result = "идентификатор заказа"
        assert main_page.check_order_id_text() == expected_result
