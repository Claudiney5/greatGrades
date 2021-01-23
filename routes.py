from flask import Flask, jsonify, request, redirect, url_for

from Controllers.grades import approval, student_average_grade

app = Flask(__name__)


@app.route("/", methods=['GET'])
def final_grades():
    templates = request.json['templates']  
    values = request.json['values']  
    students = request.json['students']    

    return jsonify({'approved': student_average_grade(students, templates, values)})


@app.route("/documentation", methods=['GET'])
def examination():
    return
    


if __name__ == '__main__':
    app.run(debug=True)