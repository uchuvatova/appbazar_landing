from selene.support.shared import browser

button_console = browser.element('.text-button-m[title="Вход в консоль"]')
button_add_app = browser.element('.CTAButton_base__Js2Q2[title="Добавить приложение"]')


class DeveloperPage:

    def open(self):
        browser.open("/developers/")

    def click_cookies(self):
        browser.element('.text-button-m').click()

    def click_enter_console(self):
        button_console.click()

    def click_add_app(self):
        button_add_app.click()
