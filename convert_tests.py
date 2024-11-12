import unittest
import convert

# Part 1
#######################################################################################################################


class TestCases(unittest.TestCase):
    # string_to_float

    # test small, single digit float
    def test_string_to_float(self):
        input_string = '2.4'
        expected = 2.4
        actual = convert.str_to_float(input_string)
        self.assertEqual(actual, expected)

    # test multiple digit float
    def test_string_to_float_negative(self):
        input_string = '243.49043'
        expected = 243.49043
        actual = convert.str_to_float(input_string)
        self.assertEqual(actual, expected)

    # test non-float
    def test_string_to_float_zero(self):
        input_string = '12.pizza'
        expected = None
        actual = convert.str_to_float(input_string)
        self.assertEqual(actual, expected)




if __name__ == '__main__':
    unittest.main()
