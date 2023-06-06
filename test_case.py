from solution import even_generator
import unittest



# Write a test class for the even_generator function that prints "Test Passed" if the function returns the expected output and "Test Failed" if it does not.

class TestEvenGenerator(unittest.TestCase):
    def test_even_generator(self):
            
        self.assertEqual (list(even_generator()),[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) # We are converting the generator object to a list and comparing it with the expected output using the assert statement


if __name__ == '__main__':
    unittest.main()
