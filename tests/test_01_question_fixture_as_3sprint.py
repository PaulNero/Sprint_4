import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

import conftest
from pages.main_page import *
from src.data import *

@allure.suite("Тестирование блока 'Вопросы о Важном'")
@allure.title(f'1. Проверка текста в ответе на важный вопрос "{q1_how_it_cost}"')
def test_how_it_cost_question(driver):
    with allure.step(f"Раскрываем вопрос: {q1_how_it_cost}"):
        WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q1_what_is_the_price_button)).click()
    with allure.step(f"Проверяем текст ответа на вопрос: {a1_how_it_cost}"):
        assert WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.a1_what_is_the_price_text)).text == a1_how_it_cost

@allure.title(f'2. Проверка текста в ответе на важный вопрос "{q2_want_several_scooters}"')
def test_several_scooters_question(driver):
    with allure.step(f"Раскрываем вопрос: {q2_want_several_scooters}"):
        WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q2_several_scooters_button)).click()
    with allure.step(f"Проверяем текст ответа на вопрос: {a2_want_several_scooters}"):
        assert WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.a2_several_scooters_text)).text == a2_want_several_scooters

@allure.title(f'3. Проверка текста в ответе на важный вопрос "{q3_how_rental_time_calculated}"')
def test_how_calculate_rental_time_question(driver):
    with allure.step(f"Раскрываем вопрос: {q3_how_rental_time_calculated}"):
        WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q3_how_is_rental_time_calculated_button)).click()
    with allure.step(f"Проверяем ответ на вопрос: {a3_how_rental_time_calculated}"):
        assert WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.a3_how_is_rental_time_calculated_text)).text == a3_how_rental_time_calculated

@allure.title(f'4. Проверка текста в ответе на важный вопрос "{q4_possible_order_scooter_today}"')
def test_can_order_today_question(driver):
    with allure.step(f"Раскрываем вопрос: {q4_possible_order_scooter_today}"):
        WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q4_order_scooter_today_button)).click()
    with allure.step(f"Проверяем ответ на вопрос: {q4_possible_order_scooter_today}"):
        assert WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.a4_order_scooter_today_text)).text == a4_possible_order_scooter_today

@allure.title(f'5. Проверка текста в ответе на важный вопрос "{q5_possible_extend_order_earlier}"')
def test_extend_order_earlier(driver):
    with allure.step(f"Раскрываем вопрос: {q5_possible_extend_order_earlier}"):
        WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q5_extend_order_button)).click()
    with allure.step(f"Проверяем ответ на вопрос: {q5_possible_extend_order_earlier}"):
        assert WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.a5_extend_order_text)).text == a5_possible_extend_order_earlier

@allure.title(f'6. Проверка текста в ответе на важный вопрос "{q6_bring_charging_with_scooter}"')
def test_chargers_with_scooter_question(driver):
    with allure.step(f"Раскрываем вопрос: {q6_bring_charging_with_scooter}"):
        WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q6_chargers_with_scooter_button)).click()
    with allure.step(f"Проверяем ответ на вопрос: {a6_bring_charging_with_scooter}"):
        assert WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.a6_chargers_with_scooter_text)).text == a6_bring_charging_with_scooter

@allure.title(f'7. Проверка текста в ответе на важный вопрос "{q7_possible_cancel_the_order}"')
def test_can_i_cancel_order_question(driver):
    with allure.step(f"Раскрываем вопрос: {q7_possible_cancel_the_order}"):
        WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q7_can_i_cancel_an_order_button)).click()
    with allure.step(f"Проверяем ответ на вопрос: {a7_possible_cancel_the_order}"):
        assert WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.a7_can_i_cancel_an_order_text)).text == a7_possible_cancel_the_order

@allure.title(f'8. Проверка текста в ответе на важный вопрос {q8_behind_MKAD_bring_me}"')
def test_live_outside_question(driver):
    with allure.step(f"Раскрываем вопрос: {q8_behind_MKAD_bring_me}"):
        WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.q8_live_outside_mkad_button)).click()
    with allure.step(f"Проверяем ответ на вопрос: {a8_behind_MKAD_bring_me}"):
        assert WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable(MainPageLocators.a8_live_outside_mkad_text)).text == a8_behind_MKAD_bring_me

