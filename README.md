<h1> Проект по тестированию лендинга Android-стора AppBazar</h1>

> <a target="_blank" href="https://appbazar.am">Ссылка на сайт</a>

![This is an image](resources/mainpage.png)

#### Список проверок, реализованных в автотестах:
- [x] Переход на страницу "О компании"
- [x] Переход на вкладку "Разработчикам"
- [x] Переход на страницу входа в консоль
- [x] Копирование ссылки
- [x] Скачивание .apk

----
### Проект реализован с использованием:

<img src="resources/python-original.svg" width="50" title="Python"> <img src="resources/pytest.png" width="50" title="Pytest"> <img src="resources/intellij_pycharm.png" width="50" title="PyCharm"> <img src="resources/selene.png" width="50" title="Selene"> <img src="resources/selenium.png" width="50" title="Selenium"> <img src="resources/selenoid.png" width="50" title="Selenoid"> <img src="resources/jenkins.png" width="50" title="Jenkins"> <img src="resources/allure_report.png" width="50" title="Allure Report"> <img src="resources/allure_testops.png" width="50" title="Allure TestOps"> <img src="resources/tg.png" width="50" title="Telegram"> <img src="resources/jira.png" width="50" title="Jira">

----
### Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/appbazar_uchuvatova/">Ссылка на проект в Jenkins</a>

#### Параметры сборки

* `environment` - параметр определяет окружение для запуска тестов
* `comment` - комментарий


#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/appbazar_uchuvatova/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Выбрать окружение в выпадающем списке
4. Указать комментарий
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](resources/jenkins_build.png)

----
### Allure отчет


#### Общие результаты
![This is an image](resources/allure_report_overview.png)
#### Список тест кейсов
![This is an image](resources/allure_test_cases.png)
#### Пример отчета о прохождении теста
![This is an image](resources/example_test_allure.png)

----

#### Тест-планы проекта
![This is an image](resources/allure_TestOps_test_plans.png)

#### Общий список всех кейсов, имеющихся в системе (без разделения по тест-планам и виду выполнения тестирования)
![This is an image](resources/allure_TestOps_test_cases.png)

#### Пример отчёта выполнения одного из автотестов
![This is an image](resources/example_autotests_allure_TestOps.png)

#### Пример dashboard с общими результатами тестирования
![This is an image](resources/allure_TestOps_dashboard.png)

----
### Интеграция с Jira
![This is an image](resources/jira_issue.png)

----
### Оповещение о результатах прогона тестов в Telegram
![This is an image](resources/tg_notification.png)

----
### Пример видео прохождения автотеста
![autotest_gif](resources/video_test.gif)