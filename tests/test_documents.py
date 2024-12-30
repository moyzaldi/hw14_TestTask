from allure_commons.types import Severity

from pages.page_documents_for_clients import DocumentsForClients
import allure

@allure.tag('Doc')
@allure.severity(Severity.CRITICAL)

def test_loading_docs_page(browser_settings):
    documents_for_clients = DocumentsForClients()

    with allure.step('Открываем страницу "Клиентские договора"'):
        documents_for_clients.open_documents_for_clients()

    with allure.step('Проверяем наличие раздела "Презентации"'):
        documents_for_clients.assert_field_presentations()

    with allure.step('Проверяем наличие раздела "Правила и условия Акций"'):
        documents_for_clients.assert_field_terms_and_conditions_of_promotions()

    with allure.step('Проверяем наличие раздела "Размещение"'):
        documents_for_clients.assert_field_placement()

    with allure.step('Проверяем наличие раздела "Печать"'):
        documents_for_clients.assert_field_print()

    with allure.step('Проверяем наличие раздела "Дизайн"'):
        documents_for_clients.assert_field_design()



