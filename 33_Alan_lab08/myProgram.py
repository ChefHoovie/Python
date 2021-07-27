import unittest
import myProgram as prog


class TestMyProgram(unittest.TestCase):

    def test_EngineType(self):
        vios = prog.Vehicle('4', 'petrol', 5, 180)
        self.assertEqual(vios.type_of_tank, 'petrol')


if __name__ == '__main__':
    unittest.main()
