from flask import Flask, jsonify
import json


data = open('data.json',)
courseFinalAvaliation = json.load(data)

students = courseFinalAvaliation['students']
templates = courseFinalAvaliation['templates']
values = courseFinalAvaliation['values']

def student_average_grade(students, templates, values):
    ''' Fornece lista(list) com média dos alunos'''
    averages = []
    for i in students:
        total_grade = 0
        for j in range(len(students[i])):
            for k in range(len(students[i][j])):
                if students[i][j][k] == templates[j][k]:
                    total_grade = total_grade + values[j][k]
        average = total_grade / len(templates)        
        averages.append(average)
    return averages    

def answers(student, answers, template, value):
    ''' Compara resposta do aluno com gabarito fornecido, aplicando o peso 
    e calculando a média final. '''
    for i in student:
        final_grade = 0
        for j in range(len(answers)-1):
            if answers[j] == template[j]:
                final_grade = final_grade + value[j]
    return (final_grade)
    

def approval( students, averages):
    ''' Compara a média final de cada aluno com a nota mínima necessária,
    relaciona os aprovados e cria json de resposta. '''
    i = 0
    approved = []
    for j in students:
        if averages[i] >= 7:
            approved.append(j)
        i = i + 1
    return approved





data.close()
