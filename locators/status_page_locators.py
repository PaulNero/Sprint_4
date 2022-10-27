from selenium.webdriver.common.by import By

class StatusPageLocators:
    status_link = "track"
    status_order_number_input = [By.XPATH, ".//input[contains(@class, 'Track_Input')]"]
    status_view_order_button = [By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Посмотреть']"]
    status_cancel_button = [By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Отменить заказ']"]
    status_confirm_cancel_button = [By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Отменить']"]
    status_unconfirm_cancel_button = [By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Назад']"]
    status_finish_cancel_button = [By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Хорошо']"]