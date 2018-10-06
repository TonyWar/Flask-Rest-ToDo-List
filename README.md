# Flask-Rest-ToDo-List
Todo list backend on Flask

### Работа с виртуальной средой
1. Создание виртуальной среды
```
python3 -m venv venv
```
2. Войти в виртуальную среду
```
source venv/bin/activate
```

###Поддержка env файлов
```
pip install python-dotenv
```
Сохранить список зависимостей
```pip freeze > requirements.txt```
Установить список зависимостей
```pip install -r requirements.txt```

### Запуск приложения
1. Сообщаем FLASK как импортировать приложение
```
export FLASK_APP=todoList.py
```
2. Запускаем
```
flask run
```

Для отладки в браузере включаем режим
```
export FLASK_DEBUG=1
```

### Миграции
Инициилизация миграции (только в первый раз)
```python migrate.py db init```
Запуск миграции
```python migrate.py db migrate```
Применение миграции
```python migrate.py db upgrade```

Если вы используете SQLite, то получившийся .db файл нужно перенести в папку app