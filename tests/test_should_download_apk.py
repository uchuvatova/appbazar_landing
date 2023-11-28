import hashlib

import allure
from allure_commons.types import Severity

from conftest import setup_browser
from pages.mainPage import MainPage


@allure.title("Скачивание apk")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "irauchuvatova")
@allure.feature("Лэндинг")
@allure.story("Пользователь скачивает apk appbazar")
@allure.link("https://appbazar.am", name="Ссылка на главную страницу")
def test_should_open_devpage(setup_browser):
    main_page = MainPage()
    with allure.step("Открыть главную страницу"):
        main_page.open()
    with allure.step("Принять куки"):
        main_page.click_cookies()
    # WHEN
    with allure.step("Нажать кнопку 'Скачать AppBazar'"):
        main_page.click_download_button()

    # THEN
    with allure.step("Проверка, что файл скачался"):
        md5 = hashlib.md5(open('1.apk', 'rb').read()).hexdigest()
