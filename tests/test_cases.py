import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.feature('Full Accounts')
@allure.story('Waiting page load')
class TestValidate:
    @allure.title('Проверка загрузки страницы')
    def test_1(self, get_driver):
        with allure.step('Переход на сайт https://effective-mobile.ru/'):
            get_driver.get('https://effective-mobile.ru/')
            time.sleep(5)
        with allure.step('Переход в блок по клику "О нас"'):
            get_driver.find_element(By.XPATH, '(//*[@class="tn-atom"])[3]').click()
            time.sleep(5)
        with allure.step('Проверить, что отображается текст "О нас"'):
            expected_text = get_driver.find_element(By.XPATH, '//*[contains(@field, "tn_text_1680508197707")]')
            assert 'о нас' in expected_text.text

        pass

    def test_2(self, get_driver):
        with allure.step('Переход на сайт https://effective-mobile.ru/'):
            get_driver.get('https://effective-mobile.ru/')
            time.sleep(5)
        with allure.step('Переход в блок по клику "Услуги"'):
            get_driver.find_element(By.XPATH, '(//*[@class="tn-atom"])[4]').click()
            time.sleep(5)
        with allure.step('Проверить, что текст раздела соответствует "Услуги"'):
            expected_text_1 = get_driver.find_element(By.XPATH, '//*[@field="tn_text_1680510339488"]')
            assert 'услуги' in expected_text_1.text

        pass

    def test_3(self, get_driver):
        with allure.step('Переход на сайт https://effective-mobile.ru/'):
            get_driver.get('https://effective-mobile.ru/')
            time.sleep(5)
        with allure.step('Переход в блок по клику "Проекты"'):
            get_driver.find_element(By.XPATH, '(//*[contains(@href, "#cases")])[2]').click()
            time.sleep(5)

        pass

    def test_4(self, get_driver):
        with allure.step('Переход на сайт https://effective-mobile.ru/'):
            get_driver.get('https://effective-mobile.ru/')
            time.sleep(5)
        with allure.step('Переход в блок по клику "Отзывы"'):
            get_driver.find_element(By.XPATH, '(//*[contains(@href, "#Reviews")])[2]').click()
            time.sleep(5)
        with allure.step('Проверить, что текст раздела соответствует "ОТЗЫВЫ КЛИЕНТОВ"'):
            expected_text_2 = get_driver.find_element(By.XPATH, '//div/strong')
            assert 'ОТЗЫВЫ КЛИЕНТОВ' in expected_text_2.text

        pass

    def test_5(self, get_driver):
        with allure.step('Переход на сайт https://effective-mobile.ru/'):
            get_driver.get('https://effective-mobile.ru/')
            time.sleep(5)
        with allure.step('Переход в блок по клику "Контакты"'):
            get_driver.find_element(By.XPATH, '(//*[@class="tn-atom"])[6]').click()
            time.sleep(5)
        with allure.step('Проверить, что текст раздела соответствует "контакты"'):
            expected_text_3 = get_driver.find_element(By.XPATH, '//*[contains(@field, "tn_text_1680516225306")]')
            assert 'контакты' in expected_text_3.text

        pass

    def test_6(self, get_driver):
        with allure.step('Переход на сайт https://effective-mobile.ru/'):
            get_driver.get('https://effective-mobile.ru/')
            time.sleep(5)
        with allure.step('Переход в блок по клику "Выбрать специалиста"'):
            get_driver.find_element(By.XPATH, '(//*[@class="tn-atom"])[7]').click()
            time.sleep(5)
        with allure.step('Проверить, что текст раздела соответствует "Наш стек"'):
            expected_text_4 = get_driver.find_element(By.XPATH, '//*[contains(text(), "Наш стек")]')
            assert 'Наш стек' in expected_text_4.text

        pass
