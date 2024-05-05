### Запустить проект локально
1. Скопировать проект
```python
git clone https://github.com/Maruf995/test_task
```

2. Сделать миграции:
```
python manage.py makemigrations
python manage.py migrate
```
3. Создать суперпользователя:
```
python manage.py createsuperuser
```
4. Запустить проект:
```
python manage.py runserver
```

Бэкенд будет доступен по адресу `http://localhost`, `http://127.0.0.1`
Админка будет доступена по адресу `http://localhost/admin`
