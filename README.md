# school_project
Мини-проект для прохождения тестирования профпригодности по методике Климова для школы:

## Технологии
* Python 3.11
* Flask==2.2.3
* Flask-SQLAlchemy==3.0.3
* Flask-Login==0.6.2

## Как запустить проект локально
Клонировать репозиторий:
```

```

Выполните по очереди команды:
```
python -m venv venv
 source venv/Scripts/activate
 python -m pip install -U pip
 pip install -r requirements.txt
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
flask load_questions
flask run
```

### Автор
AlexGriv https://github.com/AlexGriv
