from selenium.webdriver.common.by import By

class Cookie_button:
    confirm_button = [By.XPATH, ".//button[contains(@class, 'App_CookieButton')]"]

class Header_button:
    yandex_button = [By.XPATH, ".//a[@href='//yandex.ru']"]
    scooter_button = [By.XPATH, ".//a[@href='/']"]
    order_button = [By.XPATH, ".//button[@class='Button_Button__ra12g' and text()='Заказать']"]
    order_status_button = [By.XPATH, ".//button[@class='Header_Link__1TAG7']"]

class How_it_work_button:
    order_button = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp' and text()='Заказать']"]

class Questions_about_important_button:
    what_is_the_price_button = [By.XPATH, ".//div[@id='accordion__heading-16']"]
    several_scooters_button = [By.XPATH, ".//div[@id='accordion__heading-17']"]
    how_is_rental_time_calculated_button = [By.XPATH, ".//div[@id='accordion__heading-18']"]
    order_scooter_today_button = [By.XPATH, ".//div[@id='accordion__heading-19']"]
    extend_order_button = [By.XPATH, ".//div[@id='accordion__heading-20']"]
    chargers_with_scooter = [By.XPATH, ".//div[@id='accordion__heading-21']"]
    can_i_cancel_an_order = [By.XPATH, ".//div[@id='accordion__heading-22']"]
    live_outside_mkad = [By.XPATH, ".//div[@id='accordion__heading-23']"]

