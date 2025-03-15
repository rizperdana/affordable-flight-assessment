import unittest
from main import Solution
import json

class TestCheapestFlight(unittest.TestCase):
    def setUp(self):
        """Prepare test data before each test runs"""
        self.obj = Solution()

        with open("flight_data.json", "r") as file:
            self.test_data = json.load(file)

    def test_cheapest_flight_case_1(self):
        """Test with provided JSON input"""
        n = self.test_data["n"]
        flights = self.test_data["flights"]
        src = self.test_data["src"]
        dst = self.test_data["dst"]
        k = self.test_data["k"]

        result = self.obj.CheapestFLight(n, flights, src, dst, k)
        expected = 700
        self.assertEqual(result, expected)

    def test_no_possible_flight(self):
        """Test when there's no valid flight route"""
        n = 3
        flights = [[0, 1, 100], [1, 2, 200]]
        src = 0
        dst = 2
        k = 0

        result = self.obj.CheapestFLight(n, flights, src, dst, k)
        expected = -1
        self.assertEqual(result, expected)

    def test_direct_flight(self):
        """Test when there's a direct flight available"""
        n = 3
        flights = [[0, 1, 100], [1, 2, 200], [0, 2, 250]]
        src = 0
        dst = 2
        k = 1

        result = self.obj.CheapestFLight(n, flights, src, dst, k)
        expected = 250
        self.assertEqual(result, expected)

    def test_multiple_routes_same_price(self):
        """Test when there are multiple routes with the same price"""
        n = 4
        flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 3, 300]]
        src = 0
        dst = 3
        k = 2

        result = self.obj.CheapestFLight(n, flights, src, dst, k)
        expected = 300
        self.assertEqual(result, expected)

    def test_large_input(self):
        """Test with a large number of flights to check efficiency"""
        n = 100
        flights = [[i, i + 1, 10] for i in range(99)]
        src = 0
        dst = 99
        k = 98

        result = self.obj.CheapestFLight(n, flights, src, dst, k)
        expected = 990
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
