from pages.main_page import *
from pages.order_page import *

@allure.suite("Тестирование переходов на главной странице")
class TestMainPage():
    
    @allure.title('1. Проверка перехода на страницу создания заказа на самокат')
    def test_order_page_open_via_header(self, driver):
        with allure.step("Клик по кнопке оформления заказа в header"):
            MainPage(driver).get_main_page_and_order_via_header_button()
        with allure.step("Проверяем, что форма оформления заказа открылась"):
            assert driver.current_url == MainPageLocators.main_link + OrderPageLocators.order_link

    @allure.title('2. Проверка перехода на страницу создания заказа на самокат')
    def test_order_page_open_via_body(self, driver):
        with allure.step("Клик по кнопке оформления заказа в body"):
            MainPage(driver).get_main_page_and_order_via_middle_button()
        with allure.step("Проверяем, что форма оформления заказа открылась"):
            assert driver.current_url == MainPageLocators.main_link + OrderPageLocators.order_link

    @allure.title('3. Проверка перехода на главную страницу сайта заказа самокатов, через переход в форму оформления заказа')
    def test_scooter_page_open_via_header(self, driver):
        with allure.step("Клик по кнопке оформления заказа в header"):
            MainPage(driver).click_header_order_button()
        with allure.step("Клик по названию сайта 'Самокат' в header"):
            MainPage(driver).open_scooter_logo_button()
        with allure.step("Проверяем, что произошел переход на главную страницу сайта с заказом самокатов"):
            assert driver.current_url == MainPageLocators.main_link

    @allure.title('4. Проверка перехода на главную страницу сайта заказа самокатов, через страницу статуса заказа')
    def test_scooter_page_open_via_status(self, driver):
        with allure.step("Клик по кнопке 'Статус'"):
            MainPage(driver).click_status_button()
        with allure.step("Клик по названию сайта 'Самокат' в header"):
            MainPage(driver).open_scooter_logo_button()
        with allure.step("Проверяем, что произошел переход на главную страницу сайта с заказом самокатов"):
            assert driver.current_url == MainPageLocators.main_link

    @allure.title('5. Проверка перехода на главную Яндекс через клик по логотипу Яндекс')
    def test_yandex_page_open(self, driver):
        with allure.step("Клик по кнопке логотип Яндекса"):
            MainPage(driver).open_yandex_logo_button()
        with allure.step("Переключаем на вторую вкладку вкладку"):
            driver.switch_to.window(driver.window_handles[1])
        with allure.step(f"Проверяем, что URL на второй вкладке соответсвует: {MainPageLocators.dzen_link}"):
            WebDriverWait(driver, delay).until(EC.url_contains(MainPageLocators.dzen_link))
            assert driver.current_url == MainPageLocators.dzen_link

