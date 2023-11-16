from selene import have, command
from selene.support.shared import browser


class MainPage:
    def __init__(self):
        pass

    def open(self):
        browser.open("/")

    def click_link_for_developers(self):
        browser.element('[href="/developers/"]').click()

    def scroll_to_share(self):
        browser.element('//*[@id="__next"]/header/div[2]/div[5]/div[3]/div/span').perform(command.js.scroll_into_view)

    def click_copylink_button(self):
        browser.element('//*[@id="__next"]/header/div[2]/div[5]/div[3]/div/div/button/span').click


    def scroll_to_footer(self):
        browser.element('[href="/about"]').perform(command.js.scroll_into_view)

    def click_cookies(self):
        browser.element('.text-button-m').click()

    def click_about_link(self):
        browser.element('[href="/about"]').click()
