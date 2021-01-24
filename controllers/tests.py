import unittest
import json
from flask import Flask, jsonify, Response


from grades import approval, student_average_grade


class gradesTests(unittest.TestCase):

   
    def test_student_average_grade(self):
        result=json.dumps({"approved":"Cesar"})
        self.assertAlmostEqual(
            student_average_grade(
                {
                    "Cesar":[["a", "c", "d"], ["a", "e", "d"]],
                    "Cleopatra": [["e", "b", "b"], ["e", "b", "b"]],
                    "Alexandre": [["c", "c", "c"], ["c", "e", "c"]]
                },
                [["a", "b", "c"], ["a", "b", "c"]],
                [[7,2,1], [7,2,1]]
            ),
            {"approved":["Cesar"]}
        )

    def test_student_average_grade_lenght(self):
        self.assertEqual(            
            student_average_grade(
                {
                    "Cesar":[["a", "c", "d"], ["a", "e", "d"]],
                    "Cleopatra": [["e", "b", "b"], ["e", "b", "b"]],
                    "Alexandre": [["c", "c", "c"], ["c", "e", "c"]]
                },
                [["a", "b"], ["a", "b", "c"]],
                [[7,2,1], [7,2,1]]
            ),
            {'error': 'Gabarito e Valores das questões devem ter o mesmo tamanho.'}
        )
        
    def test_approval(self):
        self.assertEqual(
            approval(
                {
                    "Cesar":[["a", "c", "d"], ["a", "e", "d"]],
                    "Cleopatra": [["e", "b", "b"], ["e", "b", "b"]],
                    "Alexandre": [["c", "c", "c"], ["c", "e", "c"]]
                },
                [6.99,7.2, 7]
            ),
            ["Cleopatra", "Alexandre"]
        )

if __name__ == '__main__':
    unittest.main()
