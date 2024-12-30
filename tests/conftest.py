import allure
import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture()
def browser_settings():
    with allure.step('Параметры браузера'):
        driver_options = webdriver.ChromeOptions()
        driver_options.page_load_strategy = 'eager'
        browser.config.driver_options = driver_options
        browser.config.window_height = 1080
        browser.config.window_width = 1920
        browser.config.base_url = 'https://russoutdoor.ru/'

    yield
    with allure.step('Закрываем браузер'):
        browser.quit()

    browser.config.base_url = 'https://russoutdoor.ru/'
