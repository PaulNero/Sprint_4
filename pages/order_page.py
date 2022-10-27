

from locators.order_page_locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

delay = 10

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

### ОПИСАНИЕ ЭЛЕМЕНТОВ

    def w_is_name(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.who_is_name_input))

    def w_is_surname(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.who_is_surname_input))

    def w_is_address(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.who_is_address_input))

    def w_is_subway(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.who_is_subway_input))

    def w_is_subway_picker(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.who_is_subway_picker))

    def w_is_phone(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.who_is_phone_input))

    def order_farther(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.order_farther_button))

    def a_when_to_bring_scooter(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.about_when_to_bring_scooter_button))

    def a_rental_period(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.about_rental_period_button))

    def a_color_scooter_black(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.about_color_scooter_black_button))

    def a_color_scooter_gray(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.about_color_scooter_grey_button))

    def a_comment_for_courier(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.about_comment_for_courier_button))

    def c_confirm_create_button(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.create_order_button))

    def c_back_order_button(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.back_order_button))

    def calendar_pick_today(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.calendar_pick_today_day_button))

    def r_one_day(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.rent_one_day_button))

    def r_two_day(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.rent_two_days_button))

    def r_three_day(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.rent_three_days_button))

    def r_four_day(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.rent_four_days_button))

    def r_five_day(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.rent_five_days_button))

    def r_six_day(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.rent_six_days_button))

    def r_seven_day(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.rent_seven_days_button))

    def c_order_yes(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.confirm_order_yes_button))

    def c_order_no(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.confirm_order_no_button))

    def c_view_status(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.confirm_view_status_button))

    def c_order_number(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(OrderPageLocators.confirm_order_number_text))

### ДЕЙСТВИЯ С ЭЛЛЕМЕНТАМИ

    def set_name_input(self, name):
        self.w_is_name().send_keys(name)

    def get_name_input(self):
        self.w_is_name().get_attribute('value')

    def set_surname_input(self, surname):
        self.w_is_surname().send_keys(surname)

    def get_surname_input(self):
        self.w_is_surname().get_value()

    def set_address_input(self, address):
        self.w_is_address().send_keys(address)

    def get_address_input(self):
        self.w_is_address().get_value()

    def click_subway_input(self):
        self.w_is_subway().click()

    def set_subway_input(self, subway):
        self.w_is_subway().send_keys(subway)

    def click_subway_first_station_picker(self):
        self.w_is_subway_picker().click()

    def set_phone_number_input(self, phone):
        self.w_is_phone().send_keys(phone)

    def click_farther_button(self):
        self.order_farther().click()

    def click_when_to_bring_scooter(self):
        self.a_when_to_bring_scooter().click()

    def click_today_date_calendar(self):
        self.calendar_pick_today().click()

    def click_rental_period_field(self):
        self.a_rental_period().click()

    def click_rental_period_one_day(self):
        self.r_one_day().click()

    def click_rental_period_two_days(self):
        self.r_two_day().click()

    def click_rental_period_three_days(self):
        self.r_three_day().click()

    def click_rental_period_four_days(self):
        self.r_four_day().click()

    def click_rental_period_five_days(self):
        self.r_five_day().click()

    def click_rental_period_six_days(self):
        self.r_six_day().click()

    def click_rental_period_seven_days(self):
        self.r_seven_day().click()

    def click_black_scooter_radiobutton(self):
        self.a_color_scooter_black().click()

    def click_gray_scooter_radiobutton(self):
        self.a_color_scooter_gray().click()

    def set_comment_for_courier_input(self, comment):
        self.a_comment_for_courier().send_keys(comment)

    def click_confirm_create_order_button(self):
        self.c_confirm_create_button().click()

    def click_back_order_button(self):
        self.c_back_order_button().click()

    def click_confirm_order_yes_button(self):
        self.c_order_yes().click()

    def click_confirm_order_no_button(self):
        self.c_order_no().click()

    def click_view_status_after_order(self):
        self.c_view_status().click()

    def get_order_number_after_order(self):
        self.c_order_number().click()

### ДЕЙСТВИЯ С ГРУППОЙ ЭЛЕМЕНТОВ

    def create_order_one_day(self, name, surname, address, phone, comment):
        WebDriverWait(self.driver, delay).until(EC.
                                                element_to_be_clickable(OrderPageLocators.who_is_name_input))
        self.set_name_input(name=name)
        self.set_surname_input(surname=surname)
        self.set_address_input(address=address)
        self.click_subway_input()
        self.click_subway_first_station_picker()
        self.set_phone_number_input(phone=phone)
        self.click_farther_button()
        self.click_when_to_bring_scooter()
        self.click_today_date_calendar()
        self.click_rental_period_field()
        self.click_rental_period_one_day()
        self.click_black_scooter_radiobutton()
        self.set_comment_for_courier_input(comment=comment)
        self.click_confirm_create_order_button()
        self.click_confirm_order_yes_button()

    def create_order_five_day(self, name, surname, address, subway, phone):
        WebDriverWait(self.driver, delay).until(EC.
                                                element_to_be_clickable(OrderPageLocators.who_is_name_input))
        self.set_name_input(name=name)
        self.set_surname_input(surname=surname)
        self.set_address_input(address=address)
        self.set_subway_input(subway=subway)
        self.click_subway_first_station_picker()
        self.set_phone_number_input(phone=phone)
        self.click_farther_button()
        self.click_when_to_bring_scooter()
        self.click_today_date_calendar()
        self.click_rental_period_field()
        self.click_rental_period_five_days()
        self.click_gray_scooter_radiobutton()
        self.click_confirm_create_order_button()
        self.click_confirm_order_yes_button()