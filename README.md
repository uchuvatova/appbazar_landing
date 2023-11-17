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

<table border="2">
  <tbody>
    <tr>
        <td>Python</td>
        <td>Pytest</td>
        <td>Selene</td>
        <td>Selenium</td>
        <td>Selenoid</td>
        <td>Jenkins</td>
        <td>Allure Reports</td>
        <td>Allure TestOps</td>
        <td>Jira</td>
    </tr>
  </tbody>
</table>

<img src="resources/python-original.svg" width="50"> <img src="resources/pytest.png" width="50"> <img src="resources/intellij_pycharm.png" width="50"> <img src="resources/selene.png" width="50"> <img src="resources/selenium.png" width="50"> <img src="resources/selenoid.png" width="50"> <img src="resources/jenkins.png" width="50"> <img src="resources/allure_report.png" width="50"> <img src="resources/allure_testops.png" width="50"> <img src="resources/tg.png" width="50"> <img src="resources/jira.png" width="50">

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
![This is an image](resources/allure_report.png)
#### Пример отчета о прохождении теста
![This is an image](resources/example_test_allure.png)

----

### Полная статистика по прохождению тестпланов, отчёты и приложения к ним хранятся в Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3797/dashboards">Ссылка на проект в AllureTestOps</a> (запрос доступа `admin@qa.guru`)

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
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-955">Ссылка на проект в Jira</a>

![This is an image](resources/jira.png)

----
### Оповещение о результатах прогона тестов в Telegram
![This is an image](resources/tg_notification.png)

----
### Пример видео прохождения автотеста
![autotest_gif](resources/autotest_gif.gif)