from selenium.webdriver.common.by import By

class OrderPageLocators:
    order_link = "order"

    who_is_name_input = [By.XPATH, ".//div[2]/div[1]/input"]
    who_is_surname_input = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    who_is_address_input = [By.XPATH, ".//input[contains(@placeholder, 'Адрес')]"]
    who_is_subway_input = [By.XPATH, ".//input[contains(@placeholder, 'метро')]"]
    who_is_subway_picker = [By.XPATH, ".//li[@class='select-search__row' and @data-index = '0']"]
    who_is_phone_input = [By.XPATH, ".//input[contains(@placeholder, 'Телефон')]"]

    order_farther_button = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

    about_when_to_bring_scooter_button = [By.XPATH, ".//input[contains(@placeholder, '* Когда привезти самокат')]"]
    about_rental_period_button = [By.XPATH, ".//div[contains(text(), '* Срок аренды')]"]
    about_color_scooter_black_button = [By.XPATH, ".//label[@for='black']"]
    about_color_scooter_grey_button = [By.XPATH, ".//label[@for='grey']"]
    about_comment_for_courier_button = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]

    calendar_pick_today_day_button = [By.XPATH, ".//div[contains(@class, 'today')]"]

    rent_one_day_button = [By.XPATH, ".//div[text()='сутки']"]
    rent_two_days_button = [By.XPATH, ".//div[contains(text(), 'двое')]"]
    rent_three_days_button = [By.XPATH, ".//div[contains(text(), 'трое')]"]
    rent_four_days_button = [By.XPATH, ".//div[contains(text(), 'четверо')]"]
    rent_five_days_button = [By.XPATH, ".//div[contains(text(), 'пятеро')]"]
    rent_six_days_button = [By.XPATH, ".//div[contains(text(), 'шестеро')]"]
    rent_seven_days_button = [By.XPATH, ".//div[contains(text(), 'семеро')]"]

    create_order_button = [By.XPATH, ".//button[(text()='Заказать') and contains(@class, 'Button_Middle')]"]
    confirm_order_yes_button = [By.XPATH, ".//button[text()= 'Да']"]
    confirm_order_no_button = [By.XPATH, ".//button[text()= 'Нет']"]
    back_order_button = [By.XPATH, ".//button[(text()='Назад') and contains(@class, 'Button_Middle')]"]

    confirm_view_status_button = [By.XPATH, ".//button[text()= 'Посмотреть статус']"]
    confirm_order_number_text = [By.XPATH, ".//*/div/text()[2]"]

    complite_order_modal_window_displayed = [By.XPATH, ".//div[contains(@class, 'ModalHeader')]"]