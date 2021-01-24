from flask import Flask, jsonify, Response
import json


def student_average_grade(students, templates, values):
    ''' Fornece lista(list) com média dos alunos e envia para _approval_ que 
    responde com lista de aprovados'''

    if len(students) > 100:
        return jsonify({'error': 'Limite máximo de estudantes: 100'}), 406

    averages = []
    for i in students:
        total_grade = 0
        for j in range(len(students[i])):
            if  len(templates[j]) != len(values[j]):
                return {'error': 'Gabarito e Valores das questões devem ter o mesmo tamanho.'}
                
            for k in range(len(students[i][j])): 
                if  len(templates[j]) != len(students[i][j]):
                    return {'error': 'As respostas do aluno devem ter o mesmo tamanho que o Gabarito.'}
                if students[i][j][k] == templates[j][k]:
                    total_grade = total_grade + values[j][k]

        average = total_grade / len(templates)        
        averages.append(average) 

    return {"approved": approval(students, averages)}


def approval( students, averages):
    ''' Compara a média final de cada aluno com a nota mínima necessária,
    relaciona os aprovados e cria lista. '''
    i = 0
    approved = []
    for j in students:
        if averages[i] >= 7:
            approved.append(j)
        i = i + 1

    return approved
