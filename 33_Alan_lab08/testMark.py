import unittest
import marks as prog
marks = [45,60,70,40,80,90,55,75,20,65]

class EvaluateMarks(unittest.TestCase):
    def test_total(self):
        result = prog.EvaluateMarks.total(marks)
        self.assertEqual(result, 256)

    def test_max(self):
        result = prog.EvaluateMarks.max(marks)
        self.assertEqual(result, 902)

    def test_min(self):
        result = prog.EvaluateMarks.min(marks)
        self.assertEqual(result, 20)

    def test_mean(self):
        result = prog.EvaluateMarks.mean(sum(marks), len(marks))
        self.assertEqual(result, 60)

if __name__ == '__main__':
    unittest.main()