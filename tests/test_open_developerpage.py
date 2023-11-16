import allure
from allure_commons.types import Severity
from selene import have, browser, be

from pages.developerPage import DeveloperPage, button_console
from conftest import setup_browser
from pages.mainPage import MainPage


@allure.title("Переход на вкладку 'Разработчикам'")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "irauchuvatova")
@allure.feature("Лэндинг")
@allure.story("Пользователь переходит на страницу с информацией для разработчиков")
@allure.link("https://appbazar.am/developers/", name="Ссылка на страницу 'Разработчикам'")
def test_success_registration(setup_browser):
    main_page = MainPage()
    developer_page = DeveloperPage()
    with allure.step("Открыть главную страницу"):
        main_page.open()
    with allure.step("Принять куки"):
        main_page.click_cookies()
    # WHEN
    with allure.step("Нажать кнопку 'Разработчикам'"):
        main_page.click_link_for_developers()

    # THEN
    with allure.step("Проверка, что страница 'Разработчикам' открыта"):
        assert "https://appbazar.am/developers/" in browser.driver.current_url
        button_console.should(be.clickable)
