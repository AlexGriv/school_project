import csv

import click

from . import app, db
from .models import Testing


@app.cli.command('load_questions')
def load_questions_command():
    """Функция загрузки мнений в базу данных."""
    with open('questions.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        counter = 0
        for row in reader:
            question = Testing(**row)
            db.session.add(question)
            db.session.commit()
            counter += 1
    click.echo(f'Загружено вопросов: {counter}')
