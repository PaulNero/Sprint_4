import time
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import *
from pages.order_page import *
from pages.status_page import *


@allure.suite("Тестирование блока оформления заказа")
@pytest.mark.parametrize('name' , ['Максим', 'Михаил'])
@pytest.mark.parametrize('surname', ['Куценко','Петренко'])
@pytest.mark.parametrize('address', ['Питер 10','Питер 101'])
@pytest.mark.parametrize('subway', ['М','В'])
@pytest.mark.parametrize('phone', ['+79119910382','+79919110382'])
@pytest.mark.parametrize('comment', ['Комментарий утром','Комментарий ночью'])
def test_create_order(driver, name, surname, address, subway, phone, comment):
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(MainPageLocators.header_order_button)).click()
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.who_is_name_input)).send_keys(name)
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.who_is_surname_input)).send_keys(surname)
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.who_is_address_input)).send_keys(address)
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.who_is_subway_input)).send_keys(subway)
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.who_is_subway_picker)).click()
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.who_is_phone_input)).send_keys(phone)
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.order_farther_button)).click()
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.about_when_to_bring_scooter_button)).click()
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.calendar_pick_today_day_button)).click()
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.about_rental_period_button)).click()
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.rent_two_days_button)).click()
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.about_color_scooter_black_button)).click()
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.about_comment_for_courier_button)).send_keys(comment)
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.create_order_button)).click()
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.confirm_order_yes_button)).click()
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(OrderPageLocators.confirm_view_status_button)).click()
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(StatusPageLocators.status_cancel_button)).click()
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(StatusPageLocators.status_confirm_cancel_button)).click()
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable(StatusPageLocators.status_finish_cancel_button)).click()
