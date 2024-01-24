from flask import request, render_template

from . import app
from .models import Testing


@app.route('/', methods=['GET'])
def introduction():

    return render_template('introduction.html')


@app.route('/testing', methods=['GET'])
def testing():
    questions = Testing.query.all()
    fields = [field for field in questions]

    return render_template('testing.html', fields=fields)


@app.route('/result', methods=['GET'])
def result():
    result_nature = ''
    result_technique = ''
    result_sign = ''
    result_artistic = ''
    result_human = ''
    result = ''.join(request.args.getlist('field'))
    for i in result:
        if i == 'П':
            result_nature += i
        if i == 'Т':
            result_technique += i
        if i == 'З':
            result_sign += i
        if i == 'Х':
            result_artistic += i
        if i == 'Ч':
            result_human += i
    result_dict = {'П (природа)': len(result_nature),
                   'Т (техника)': len(result_technique),
                   'З (знак)': len(result_sign),
                   'Х (художественный образ)': len(result_artistic),
                   'Ч (человек)': len(result_human)
                   }
    return render_template('result.html',  result=result, result_dict=result_dict)
