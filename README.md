# school_project
Мини-проект для прохождения тестирования профпригодности по методике Е.А.Климова для школы:

## Технологии
* Python 3.11
* Flask==2.2.3
* Flask-SQLAlchemy==3.0.3


## Как запустить проект локально
Клонировать репозиторий:
```
https://github.com/AlexGriv/school_project.git
```

Выполните по очереди команды:
```
python -m venv venv
 source venv/Scripts/activate
 python -m pip install -U pip
 pip install -r requirements.txt
flask db init
flask db migrate -m "Name migration"
flask db upgrade
```
flask load_questions
flask run
```
### Автор
AlexGriv https://github.com/AlexGriv
