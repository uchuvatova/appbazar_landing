import allure
from allure_commons.types import Severity
from selene import browser

from pages.developerpage import DeveloperPage
from conftest import setup_browser


@allure.title("Переход на страницу входа в консоль кнопкой 'Войти в консоль'")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "irauchuvatova")
@allure.feature("Landing")
@allure.story("Пользователь переходит на страницу консоли разработчика")
@allure.link("https://developer.appbazar.am/login", name="Страница входа в консоль")
def test_should_redirect_to_console(setup_browser):
    developer_page = DeveloperPage()
    with allure.step("Открыть страницу для разработчиков"):
        developer_page.open()
    with allure.step("Принять куки"):
        developer_page.click_cookies()
    # WHEN
    with allure.step("Нажать на кнопку 'Войти в консоль'"):
        developer_page.click_enter_console()

    # THEN
    with allure.step("Проверка открытия страницы входа в консоль"):
        assert "https://developer.appbazar.am" in browser.driver.current_url
