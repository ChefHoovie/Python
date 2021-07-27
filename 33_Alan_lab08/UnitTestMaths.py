import unittest
import operationMaths as prog

class TestMyProgram(unittest.TestCase):

    def test_add(self):
        result = prog.MathsOperation.add(5, 6)
        self.assertEqual(result, 11)

    def test_minus(self):
        result = prog.MathsOperation.minus(10, 6)
        self.assertEqual(result, 4)

