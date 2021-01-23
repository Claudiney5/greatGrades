import unittest
from grades import answers, approval, student_average_grade


class gradesTests(unittest.TestCase):
    
    def test_answers(self):
        self.assertEqual(
            answers(["Napoleão"], ["a", "b", "d"], ["a", "b", "d"], [1, 2, 3] ),
            3
        )
    
    def test_student_average_grade(self):
        self.assertEqual(
            student_average_grade(
                {
                    "Cesar":[["a", "c", "d"], ["a", "e", "d"]],
                    "Cleopatra": [["e", "b", "b"], ["e", "b", "b"]],
                    "Alexandre": [["c", "c", "c"], ["c", "e", "c"]]
                },
                [["a", "b", "c"], ["a", "b", "c"]],
                [[3,2,1], [3,2,1]]
            ),
            [3,2,1]
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
