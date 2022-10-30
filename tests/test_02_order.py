from pages.main_page import *
from pages.order_page import *

@allure.suite("Тестирование блока оформления заказа")
class TestOrderPage():

    @allure.title("1. Проверка создания заказа на самокат, через кнопку 'Заказать' в header сайта")
    def test_positive_order_via_header_button(self, driver):
        with allure.step("Клик по кнопке 'Заказать' в header"):
            MainPage(driver).click_header_order_button()
        with allure.step("Заполняем форму заказа:"):
            OrderPage(driver).create_order_one_day(name="Павел",
                                                        surname="Неробов",
                                                        address="Минск",
                                                        phone="+79119910382",
                                                        comment="Спасибо")
        with allure.step("Проверяем, что форма заказа заполнена и открылась модалка после оформления заказа"):
            assert driver.find_element(*OrderPageLocators.complite_order_modal_window_displayed).is_displayed()

    @allure.title("2. Проверка создания заказа на самокат, через кнопку 'Заказать' в теле сайта")
    def test_positive_order_via_page_button(self, driver):
        with allure.step("Клик по кнопке 'Заказать' в body"):
            MainPage(driver).click_body_order_button()
        with allure.step("Заполняем форму заказа:"):
            OrderPage(driver).create_order_five_day(name="Пабло",
                                                        surname="Никробиус",
                                                        address="Москва",
                                                        subway="ав",
                                                        phone="+79919110382")
        with allure.step("Проверяем, что форма заказа заполнена и открылась модалка после оформления заказа"):
            assert driver.find_element(*OrderPageLocators.complite_order_modal_window_displayed).is_displayed()


