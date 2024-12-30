from selene import browser, have

class DocumentsForClients:

    def open_documents_for_clients(self):
        browser.open('clients/docs/')

    def assert_field_terms_and_conditions_of_promotions(self):
        browser.element('.collapsible-container').should(have.text('Правила и условия Акций'))

    def assert_field_presentations(self):
        browser.element('.collapsible-container').should(have.text('Презентации'))

    def assert_field_placement(self):
        browser.element('.collapsible-container').should(have.text('Размещение'))

    def assert_field_print(self):
        browser.element('.collapsible-container').should(have.text('Печать'))

    def assert_field_design(self):
        browser.element('.collapsible-container').should(have.text('Дизайн'))