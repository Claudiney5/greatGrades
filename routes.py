from flask import Flask, jsonify, request, redirect, url_for

from Controllers.grades import answers, approval, student_average_grade

app = Flask(__name__)


@app.route("/", methods={'GET', ' POST'})
def final_grades():
    course = request.json['course'] 
    templates = request.json['templates']  
    values = request.json['values']  
    students = request.json['students']

    print(students)

    return "Página inicial", 200

@app.route("/documentation", methods=['get'])
def examination():
    
    return
    


if __name__ == '__main__':
    app.run(debug=True)