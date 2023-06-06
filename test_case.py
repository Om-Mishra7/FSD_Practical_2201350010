from solution import even_generator



# Write a test class for the even_generator function that prints "Test Passed" if the function returns the expected output and "Test Failed" if it does not.

class TestEvenGenerator:
    def test_even_generator(self):
        
        try:
            assert list(even_generator()) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] # We are converting the generator object to a list and comparing it with the expected output using the assert statement
            return "Test Passed"
        
        except AssertionError: # If the assert statement fails, then the AssertionError is raised
            return "Test Failed"
        
        

# Create an instance of the test class
test = TestEvenGenerator()

# Call the test method and print the output
print(test.test_even_generator())