from flask import Flask, jsonify, request, redirect, url_for, Response, render_template
from controllers.grades import approval, student_average_grade
import json

app = Flask(__name__)


@app.route("/", methods=['GET'])
def final_grades():
    templates = request.json['templates']  
    values = request.json['values']  
    students = request.json['students']    

    approved = student_average_grade(students, templates, values)

    if 'error' in approved:
        status = 406
    else:
        status = 200

    result=json.dumps(approved)

    return Response(result, status=status, mimetype='application/json')


@app.route("/docs", methods=['GET'])
def examination():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)