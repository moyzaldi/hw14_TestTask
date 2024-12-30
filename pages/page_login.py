from selene import browser, by, have, be

class UserAuthorization:
    def open_page_login(self):
        browser.open('https://online.russoutdoor.ru/')
        browser.element('.russ-header-buttons').element(by.text('Вход')).click()

    def fill_login(self, value):
        browser.element('input[type="email"]').should(be.blank).type(value)

    def fill_password(self, value):
        browser.element('input[type="password"]').should(be.blank).type(value)

    def submit(self):
        browser.element('.login-form-buttons > [aria-label="Вход"]').click()

    def assert_field_request_code(self):
        browser.element('[name=requestCode]').should(be.visible)

    def assert_no_field_request_code(self):
        browser.element('[name=requestCode]').should(be.not_.visible)

    def assert_text_incorrect_authorization_data(self):
        browser.element('.login-form-container').should(have.text('Неверный Email или пароль'))
