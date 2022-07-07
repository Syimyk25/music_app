# 1. Работа с виртуальным окружением

"""

python3 -m venv (venv) - создаем виртуальное окружение (в скобках название)

source venv/bin/activate - активируем

pip freeze - список установленных библиотек

deactivate - выйти из виртуального окружения

"""

# 2. создание файлса с библиотеками
"""
какие библиотеки нужны для это программы

requirements.txt
    django
    djangorestframework
"""

# 3. установка библиотек с файла
"""
pip install -r requirements.txt - установка библиотек
"""

# 4. создание главного проекта
"""
django-admin startproject (name_project) . - создаем главное приложение нашего проекта

. (точка) избегаем вложенностей
"""

# 5 создание приложения
"""
django-admin startapp (name_app) - создаем определенное приложение
./manage.py startapp (name_app) - второй вариант создания
"""

"""
    создать логику в models
    добавить в settings.py / INSTALLED_APPS
    импортировать и зарегестрировать в admin
"""

# 6 миграция
"""
переносим свои изменения в БД

./manage.py makemigrations - создает миграцию, фиксируем изменения
./manage.py migrate - применяет ее, заносит в БД изменения
"""

# 7 superuser
"""
./manage.py createsuperuser - создает суперюзе

"""

# 8. запуск
"""
./manage.py runserver
"""







# папки в майн апп
"""
__init__.py - говорит что это пакет
urld.py - прописываем н поинты
"""