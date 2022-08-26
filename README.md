# stepik_auto_tests_course_rep2
0. В этом репозитории хранится файлы conftest.py и test_items.py в папке - test_lesson3_6_step9_fixture.py 
для рецензирования в рамка степа - https://stepik.org/lesson/237240/step/9?unit=209628; 
1. Тестирование кода в файлах conftest.py и test_items.py проводилось в PyCharm Community Edition 2022.1.3, Python Interpreter: Python 3.10
2. Добавлены используемые в коде файлов conftest.py и test_items.py вэбдрайверы - chromedriver.exe и geckodriver.exe в папке webdrivers;
3. Добавлен файл с перечнем пакетов библиотек requirements.txt на случай возможных конфликтов в исполняем коде файлов;
4. В файле test_items.py добавлены закомментированные import time и команда time.sleep(30) исключительно для  удобства рецензентов;
5. Селектор применяем для поиска кнопки - "Добавить в корзину" в файле test_items.py уникален только для проверяемой страницы с точки зрения критерия приемки такой селектор является валидным;
6. Тест в локальном репозитории для конкретного языка можно запустить например командами pytest --language=es test_items.py, --language=fr test_items.py
7. По умолчанию в parser.addoption для language - default="ru";
8. Так же проводилась проверка для языков скр. - ru, de, zh - тест успешно проходит;  
9. Тест в локальном репозитории можно запустить командами pytest --language=es test_items.py, --language=fr test_items.py в рамках критериев приемки; 
10. По умолчанию в parser.addoption для browser_name - default="chrome";
11. Тест в локальном репозитории для конкретного языка или браузера firefox, можно запустить например командами pytest --language=es test_items.py, --browser_name=firefox
12. Для Firefox объявление нужного языка в файле conftest.py использовалась конструкция для Firefox из степа - https://stepik.org/lesson/237240/step/8?unit=209628
13. При запуске теста для --browser_name=firefox с передачей языка через командную строку тест проходит с предупреждениями - не стал эксперементировать с отладкой теста т.к. ожидаемый критерий приемки включает тест только для --browser_name=chrome
 