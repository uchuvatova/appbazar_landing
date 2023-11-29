import allure
from allure_commons.types import Severity
from selene.support.shared import browser

from conftest import setup_browser
from pages.mainpage import MainPage


@allure.title("Открытие страницы с нормативными документами")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "irauchuvatova")
@allure.feature("Landing")
@allure.story("Пользователь открывает страницу с нормативными документами")
@allure.link("https://appbazar.am/about/", name="Ссылка на страницу с нормативными документами")
def test_should_open_aboutpage(setup_browser):
    main_page = MainPage()

    with allure.step("Открыть главную страницу"):
        main_page.open()

    # WHEN
    with allure.step("Скролл до футера страницы"):
        main_page.scroll_to_footer()
    with allure.step("Принять куки"):
        main_page.click_cookies()
    with allure.step("Нажать на ссылку 'О компании'"):
        main_page.click_about_link()

    # THEN
    with allure.step("Проверка, что страница 'О компании' открыта"):
        assert "https://appbazar.am/about" in browser.driver.current_url