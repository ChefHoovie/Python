import unittest
import myVehicle as prog


class TestMyProgram(unittest.TestCase):

    def test_EngineType(self):
        vios = prog.Vehicle('4', 'petrol', 5, 180)
        self.assertEqual(vios.type_of_tank, 'petrol')


class Vehicle:
    def __init__(self,number_of_wheels,type_of_tank,seating_capacity,maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    def drive(self):
        print("The vehicle is in driving mode now")

vios = Vehicle(4,"petrol",5,180)
vios.drive()

if __name__ == '__main__':
    unittest.main()
