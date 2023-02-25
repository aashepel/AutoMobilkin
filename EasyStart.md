# AutoMobilkin

1. Установить Python (если не установлен) - https://www.python.org/downloads/  
2. Установить PyCharm Professional Edition  
3. Рекомендую установить плагин One Dark Theme (File --> Settings --> Plugins)  
4. File --> New Project --> Create  ![image](https://user-images.githubusercontent.com/67122995/221321506-a1bb6d12-07bc-41fb-b1b5-42071e8e6a55.png)  
5. Создать файл .gitignore в корневой папке проекта с следующим содержанием: https://github.com/aashepel/AutoMobilkin/blob/master/.gitignore  
6. Создать файл .env в корневой папке проекта с следующим содержанием (вместо белых полос ваши данные):  ![Скриншот 25-02-2023 024713](https://user-images.githubusercontent.com/67122995/221322159-ed2297e0-0dd5-4730-bd8e-6faa5dd3c1d8.jpg)  
6.1. SECRET_KEY - Ключ Django, к БД не относится. Сгенерировать можно тут: https://djecrety.ir/  
7. Установить пакеты в виртуальное окружение  
7.1. В правом нижнем углу нажать на Python 3.11 (в скобках название проекта) --> Interpreter Settings  ![image](https://user-images.githubusercontent.com/67122995/221322524-1a78912f-ba0b-4503-a831-19d0f48d0389.png)  
7.2. Нажать "+"  ![image](https://user-images.githubusercontent.com/67122995/221322812-a10cdacf-4bd2-466c-b486-867e274e19bc.png)  
7.3. Установить пакет python-decouple  
7.4. Установить пакет Pillow  
7.5. Установить пакет psycopg2  
8. Нажать Terminal в нижней части экрана на панели  
8.1. ввести: **pip install django**

# Миграции
После создания моделей в файле models.py можно приступить к созданию миграции.  
Создание миграции выполняется командой в терминале, находясь в корневой папке проекта: **python manage.py makemigrations**
Применение миграции на БД выполняется командой в терминале, находясь в коневой папке проекта: **python manage.py migrate**



