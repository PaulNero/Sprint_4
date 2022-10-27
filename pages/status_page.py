import time
from locators.status_page_locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

delay = 10

class StatusPage:
    def __init__(self, driver):
        self.driver = driver

### ОПИСАНИЕ ЭЛЕМЕНТОВ

    def status_order_input(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(StatusPageLocators.status_order_number_input))

    def status_view_order_button(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(StatusPageLocators.status_view_order_button))

    def status_cancel_order_button(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(StatusPageLocators.status_cancel_button))

    def status_confirm_cancel_button(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(StatusPageLocators.status_confirm_cancel_button))

    def status_unconfirm_cancel_button(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(StatusPageLocators.status_unconfirm_cancel_button))

    def status_finish_cancel_button(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(StatusPageLocators.status_finish_cancel_button))



### ДЕЙСТВИЯ С ЭЛЛЕМЕНТАМИ

    def status_set_order_number_input(self, number):
        self.status_order_input().send_keys(number)

    def status_get_order_number_input(self):
        self.status_order_input().get_value()

    def status_click_view_order_button(self):
        self.status_view_order_button().click()

    def status_click_cancel_order_button(self):
        self.status_cancel_order_button().click()

    def status_click_confirm_cancel_button(self):
        self.status_confirm_cancel_button().click()

    def status_click_unconfirm_cancel_button(self):
        self.status_unconfirm_cancel_button().click()

    def status_click_finish_cancel_button(self):
        self.status_finish_cancel_button().click()