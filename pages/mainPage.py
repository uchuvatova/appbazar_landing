import os

import requests
from selene import have, command, query
from selene.support.shared import browser

from paths import RESOURCES_PATH


class MainPage:
    def __init__(self):
        pass

    def open(self):
        browser.open("/")

    def click_link_for_developers(self):
        browser.element('[href="/developers/"]').click()

    def click_download_button(self):
        browser.element('[href="https://appbazar.am/apk"]').click()
        href = browser.element('[href="https://appbazar.am/apk"]').get(query.attribute("href"))
        content = requests.get(href).content
        with open(os.path.join(RESOURCES_PATH, '1.apk'), 'wb') as f:
            f.write(content)

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
