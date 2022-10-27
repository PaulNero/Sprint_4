from selenium.webdriver.common.by import By


class MainPageLocators:
    main_link = "https://qa-scooter.praktikum-services.ru/"
    dzen_link = "https://dzen.ru/?yredirect=true"
    cookie_confirm_button = [By.XPATH, ".//button[contains(@class, 'App_CookieButton')]"]

    header_yandex_button = [By.XPATH, ".//a[@href='//yandex.ru']"]
    header_scooter_button = [By.XPATH, ".//a[@href='/']"]
    header_order_button = [By.XPATH, ".//button[@class='Button_Button__ra12g' and text()='Заказать']"]
    header_order_status_button = [By.XPATH, ".//button[@class='Header_Link__1TAG7']"]

    how_it_work_order_button = [By.XPATH, ".//div/div/div/div/div/div/button[text()='Заказать']"]

    q1_what_is_the_price_button = [By.XPATH, ".//div[text()='Сколько это стоит? И как оплатить?']"]
    q2_several_scooters_button = [By.XPATH, ".//div[text()='Хочу сразу несколько самокатов! Так можно?']"]
    q3_how_is_rental_time_calculated_button = [By.XPATH, ".//div[text()='Как рассчитывается время аренды?']"]
    q4_order_scooter_today_button = [By.XPATH, ".//div[text()='Можно ли заказать самокат прямо на сегодня?']"]
    q5_extend_order_button = [By.XPATH, ".//div[text()='Можно ли продлить заказ или вернуть самокат раньше?']"]
    q6_chargers_with_scooter_button = [By.XPATH, ".//div[text()='Вы привозите зарядку вместе с самокатом?']"]
    q7_can_i_cancel_an_order_button = [By.XPATH, ".//div[text()='Можно ли отменить заказ?']"]
    q8_live_outside_mkad_button = [By.XPATH, ".//div[text()='Я жизу за МКАДом, привезёте?']"]

    a1_what_is_the_price_text = [By.XPATH, f".//p[contains(text(), '400')]"]
    a2_several_scooters_text = [By.XPATH, ".//p[contains(text(), 'один заказ')]"]
    a3_how_is_rental_time_calculated_text = [By.XPATH, ".//p[contains(text(), 'заказ на 8 мая')]"]
    a4_order_scooter_today_text = [By.XPATH, ".//p[contains(text(), 'расторопнее')]"]
    a5_extend_order_text = [By.XPATH, ".//p[contains(text(), '1010')]"]
    a6_chargers_with_scooter_text = [By.XPATH, ".//p[contains(text(), 'Зарядка')]"]
    a7_can_i_cancel_an_order_text = [By.XPATH, ".//p[contains(text(), 'Штрафа')]"]
    a8_live_outside_mkad_text = [By.XPATH, ".//p[contains(text(), 'И Москве')]"]

