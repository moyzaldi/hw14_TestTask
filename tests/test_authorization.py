import pytest
import allure
from allure_commons.types import Severity

from pages.page_login import UserAuthorization

@allure.tag('Auth')
@pytest.fixture(autouse=True)
def opening_the_authorization_form(browser_settings):
    user_authorization = UserAuthorization()

    with allure.step('Открываем страницу входа в РО'):
        user_authorization.open_page_login()


@allure.severity(Severity.CRITICAL)
@allure.tag('Auth')
def test_code_request_with_login_and_password(browser_settings):
    user_authorization = UserAuthorization()

    with allure.step('Вводим  логин'):
        user_authorization.fill_login('rollingmarci@freesourcecodes.com')

    with allure.step('Вводим  пароль'):
        user_authorization.fill_password('qWERTY123!')

    with allure.step('Запрашиваем код пароль'):
        user_authorization.submit()

    with allure.step('Проверяем наличие поля "код пароль'):
        user_authorization.assert_field_request_code()


@allure.severity(Severity.CRITICAL)
@allure.tag('Auth')
def test_code_request_with_wrong_login(browser_settings):
    user_authorization = UserAuthorization()

    with allure.step('Вводим неверный логин'):
        user_authorization.fill_login('rollingmarci@freesourcecods.com')

    with allure.step('Вводим неверный пароль'):
        user_authorization.fill_password('qWERTY123!')

    with allure.step('Запрашиваем код пароль'):
        user_authorization.submit()

    with allure.step('Проверяем отсутствие поля "код пароль'):
        user_authorization.assert_no_field_request_code()

    with allure.step('Проверяем текст,  что введены неправильные данные'):
        user_authorization.assert_text_incorrect_authorization_data()


@allure.severity(Severity.CRITICAL)
@allure.tag('Auth')
def test_code_request_with_wrong_password(browser_settings):
    user_authorization = UserAuthorization()

    with allure.step('Вводим  логин'):
        user_authorization.fill_login('rollingmarci@freesourcecods.com')

    with allure.step('Вводим  пароль'):
        user_authorization.fill_password('qWERTY1dasd23!')

    with allure.step('Запрашиваем код пароль'):
        user_authorization.submit()

    with allure.step('Проверяем отсутствие поля "код пароль'):
        user_authorization.assert_no_field_request_code()

    with allure.step('Проверяем текст,  что введены неправильные данные'):
        user_authorization.assert_text_incorrect_authorization_data()


@allure.severity(Severity.CRITICAL)
@allure.tag('Auth')
def test_code_request_without_login_password(browser_settings):
    user_authorization = UserAuthorization()

    with allure.step('Запрашиваем код пароль'):
        user_authorization.submit()

    with allure.step('Проверяем отсутствие поля "код пароль'):
        user_authorization.assert_no_field_request_code()
