from selene.support.shared import browser

button_console = browser.element('.text-button-m[title="Вход в консоль"]')
class DeveloperPage:

    def __init__(self):
        pass

    def open(self):
        browser.open("/developers/")

    def click_cookies(self):
        browser.element('.text-button-m').click()

    def click_enter_console(self):
        button_console.click()
