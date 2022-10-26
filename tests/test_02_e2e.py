import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import *
from pages.order_page import *
from pages.status_page import *


@allure.suite("Тестирование блока оформления заказа")
class TestEnd2EndOrderPage():

    driver = None

    @classmethod
    def setup_class(self):
        with allure.step(f"Запускаем браузер и переходим на {MainPageLocators.main_link}"):
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
            self.driver.set_window_size(1920, 1080)
            self.driver.get(MainPageLocators.main_link)
            MainPage(self.driver).click_confirm_cookie_button()

    @allure.title("1. Проверка создания заказа на самокат, через кнопку 'Заказать' в header сайта")
    def test_open_order_modal_page(self):
        with allure.step("Клик по кнопке 'Заказать' в header"):
            MainPage(self.driver).click_header_order_button()
        assert OrderPageLocators.order_link in self.driver.current_url

    def test_input_name_field(self):
        with allure.step("Заполняем поле Имя"):
            OrderPage(self.driver).set_name_input(name="Имя")
        with allure.step("Проверяем поле Имя"):
            assert self.driver.find_element(
                *OrderPageLocators.who_is_name_input).get_attribute('value') == "Имя"

    def test_input_surname_field(self):
        with allure.step("Заполняем поля Фамилия"):
            OrderPage(self.driver).set_surname_input(surname="Фамилия")
        with allure.step("Проверяем поле Фамилия"):
            assert self.driver.find_element(
                *OrderPageLocators.who_is_surname_input).get_attribute('value') == "Фамилия"

    def test_input_address_field(self):
        with allure.step("Заполняем поле Адрес"):
            OrderPage(self.driver).set_address_input(address="Адрес 10 2")
        with allure.step("Проверяем поле Адрес"):
            assert self.driver.find_element(
                *OrderPageLocators.who_is_address_input).get_attribute('value') == "Адрес 10 2"

    def test_input_subway_field(self):
        with allure.step("Вписываем метро в инпут"):
            OrderPage(self.driver).set_subway_input(subway="Крас")
        with allure.step("Клик по первому элементу в списке"):
            OrderPage(self.driver).click_subway_first_station_picker()

    def test_input_phone_field(self):
        with allure.step("Заполняем поле Номера телефона"):
            OrderPage(self.driver).set_phone_number_input(phone="+79119910382")
        with allure.step("Проверяем поле Номера телефона"):
            assert self.driver.find_element(
                *OrderPageLocators.who_is_phone_input).get_attribute('value') == "+79119910382"

    def test_go_to_next_page(self):
        with allure.step("Переходим на следующий экран"):
            OrderPage(self.driver).click_farther_button()

    def test_open_calendar_to_choose_bring_date(self):
        with allure.step("Открываем календарь для выбора даты доставки самоката"):
            OrderPage(self.driver).click_when_to_bring_scooter()
        with allure.step("Выбираем сегодняшнюю дату"):
            OrderPage(self.driver).click_today_date_calendar()

    def test_rental_period(self):
        with allure.step("Открываем выпадающее меню выбора срока аренды"):
            OrderPage(self.driver).click_rental_period_field()
        with allure.step("Выбираем срок аренды"):
            OrderPage(self.driver).click_rental_period_one_day()

    def test_choose_scooter_color(self):
        with allure.step("Выбираем цвет самоката"):
            OrderPage(self.driver).click_gray_scooter_radiobutton()

    def test_input_comment_field(self):
        with allure.step("Заполняем поле комментарий для курьера"):
            OrderPage(self.driver).set_comment_for_courier_input(comment="Комметрий")
        with allure.step("Проверяем поле комментарий для курьера"):
            assert self.driver.find_element(
                *OrderPageLocators.about_comment_for_courier_button).get_attribute('value') == "Комметрий"

    def test_click_button_create_order(self):
        with allure.step("Клик по кнопке заказать"):
            OrderPage(self.driver).click_confirm_create_order_button()
        with allure.step("Подтверждение создания заказа"):
            OrderPage(self.driver).click_confirm_order_yes_button()

    def test_open_status_page(self):
        with allure.step("Открываем окно статуса"):
            OrderPage(self.driver).click_view_status_after_order()
        with allure.step("Проверяем редирект на страницу проверку статуса"):
            assert StatusPageLocators.status_link in self.driver.current_url

    def test_cancel_order(self):
        with allure.step("Отменить заказ"):
            StatusPage(self.driver).status_click_cancel_order_button()

    def test_confirm_cancel_order(self):
        with allure.step("Подтверждаем отмену заказа"):
            StatusPage(self.driver).status_click_confirm_cancel_button()

    def test_finish_cancel_order(self):
        with allure.step("Закрываем модалку после успешной отмены заказа"):
            StatusPage(self.driver).status_click_finish_cancel_button()
        with allure.step("Проверяем редирект на главную после отмены заказа"):
            assert self.driver.current_url == MainPageLocators.main_link

    @classmethod
    def teardown_class(cls):
        with allure.step("Закрытие браузера"):
            cls.driver.quit()

