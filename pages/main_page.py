import time
from locators.main_page_locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


delay = 10

class MainPage:
    def __init__(self, driver):
        self.driver = driver

### ОПИСАНИЕ ЭЛЕМЕНТОВ

    def confirm_cookie(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.cookie_confirm_button))

    def h_logo_yandex(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.header_yandex_button))

    def h_logo_scooter(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.header_scooter_button))

    def h_order(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.header_order_button))

    def h_order_status(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.header_order_status_button))

    def how_it_work_order(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.how_it_work_order_button))

    def q1_what_is_price(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q1_what_is_the_price_button))

    def q2_several_scooters(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q2_several_scooters_button))

    def q3_how_is_rental_time(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q3_how_is_rental_time_calculated_button))

    def q4_order_scooter_today(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q4_order_scooter_today_button))

    def q5_extend_order(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q5_extend_order_button))

    def q6_chargers_with_scooter(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q6_chargers_with_scooter_button))

    def q7_can_i_cancel_an_order(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q7_can_i_cancel_an_order_button))

    def q8_live_outside_mkad(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q8_live_outside_mkad_button))

##### ДЕЙСТВИЯ С ЭЛЕМЕНТАМИ
    @allure.step('Закрыли подтверждение cookie')
    def click_confirm_cookie_button(self):
        self.confirm_cookie().click()

    def click_yandex_logo_button(self):
        self.h_logo_yandex().click()

    def click_scooter_logo_button(self):
        self.h_logo_scooter().click()

    def click_header_order_button(self):
        self.h_order().click()

    def click_status_button(self):
        self.h_order_status().click()

    def click_body_order_button(self):
        self.how_it_work_order().click()

    def click_what_is_price_question(self):
        self.q1_what_is_price().click()

    def click_several_scooters_question(self):
        self.q2_several_scooters().click()

    def click_how_is_rental_time_question(self):
        self.q3_how_is_rental_time().click()

    def click_order_scooter_today_question(self):
        self.q4_order_scooter_today().click()

    def click_extend_order_question(self):
        self.q5_extend_order().click()

    def click_chargers_with_scooter_question(self):
        self.q6_chargers_with_scooter().click()

    def click_how_cancel_order_question(self):
        self.q7_can_i_cancel_an_order().click()

    def click_live_outside_mkad(self):
        self.q8_live_outside_mkad().click()

##### ДЕЙСТВИЯ С НЕСКОЛЬКИМИ ЭЛЛЕМЕНТАМИ

    def confirm_cookie_button_and_open_order_page(self):
        self.click_confirm_cookie_button()
        self.click_header_order_button()

    def get_main_page_and_order_via_header_button(self):
        # self.driver.get(MainPageLocators.main_link)
        self.click_header_order_button()

    def get_main_page_and_order_via_middle_button(self):
        # self.driver.get(MainPageLocators.main_link)
        # WebDriverWait(self.driver, delay).until(EC.url_to_be(MainPageLocators.main_link))
        # WebDriverWait(self.driver, delay).until(EC.
        #                                         element_to_be_clickable(MainPageLocators.how_it_work_order_button))
        self.click_body_order_button()

    def open_yandex_logo_button(self):
        self.driver.get(MainPageLocators.main_link)
        self.click_yandex_logo_button()

    def open_scooter_logo_button(self):
        self.driver.get(MainPageLocators.main_link)
        self.click_scooter_logo_button()

