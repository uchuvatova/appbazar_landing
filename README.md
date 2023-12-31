<h1> Тестирование лендинга Android-стора AppBazar</h1>

> <a target="_blank" href="https://appbazar.am">Ссылка на сайт</a>

![This is an image](resources/mainpage.png)

#### Список проверок, реализованных в автотестах:
- [x] Переход на страницу "О компании"
- [x] Переход на вкладку "Разработчикам"
- [x] Переход на страницу входа в консоль кнопкой "Войти в консоль"
- [x] Переход на страницу входа в консоль кнопкой "Добавить приложение"
- [x] Скачивание apk-файла

----
### Проект реализован с использованием:

<img src="resources/icons/python-original.svg" width="50" title="Python"> <img src="resources/icons/pytest.png" width="50" title="Pytest"> <img src="resources/icons/intellij_pycharm.png" width="50" title="PyCharm"> <img src="resources/icons/selene.png" width="50" title="Selene"> <img src="resources/icons/selenium.png" width="50" title="Selenium"> <img src="resources/icons/selenoid.png" width="50" title="Selenoid"> <img src="resources/icons/jenkins.png" width="50" title="Jenkins"> <img src="resources/icons/allure_report.png" width="50" title="Allure Report"> <img src="resources/icons/allure_testops.png" width="50" title="Allure TestOps"> <img src="resources/icons/tg.png" width="50" title="Telegram"> <img src="resources/icons/jira.png" width="50" title="Jira">

----
### Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/appbazar_uchuvatova/">Ссылка на проект в Jenkins</a>

#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/appbazar_uchuvatova/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Выбрать окружение в выпадающем списке ENVIRONMENT
4. Указать комментарий в поле COMMENT
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure

<img alt="This is an image" src="resources/jenkins_build.png" width="300"/>

----
### Allure-отчет


#### Общие результаты
![This is an image](resources/allure_report_overview.png)
#### Список тест-кейсов
![This is an image](resources/allure_test_cases.png)
#### Пример отчета о прохождении теста

<img alt="This is an image" height="300" src="resources/example_test_allure.png"/>

----
### Allure TestOps

#### Общий список всех кейсов, имеющихся в системе
![This is an image](resources/allure_TestOps_test_cases.png)

#### Пример dashboard с общими результатами тестирования
![This is an image](resources/allure_TestOps_dashboard.png)

----
### Интеграция с Jira
![This is an image](resources/jira_issue.png)

----
### Оповещение о результатах прохождения тестов в Telegram

<img alt="This is an image" height="250" src="resources/tg_notification.png"/>

----
### Пример видео прохождения автотеста

![Открытие страницы с нормативными документами](resources/video_test.gif)