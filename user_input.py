class UserNumbers:

    def __init__(self, user_input):
        if isinstance(user_input, (list, int)):
            self.numbers = user_input
        elif isinstance(user_input, str):
            numbers = user_input.split()
            try:
                self.numbers = [int(n) for n in numbers]
            except ValueError as e:
                raise ValueError(f"Invalid input: {e}")
            

    def reversed(self):
        return list(reversed(self.numbers))
    

    def max(self):
        return max(self.numbers)
    
    def min(self):
        return min(self.numbers)
    
    def printable(self):
        return str(self.numbers)
    

import unittest

#main unittest class
class TestUserInput(unittest.TestCase):

    def test_user_numbers(self):                            
        numbers = UserNumbers("1 2 3")
        self.assertEqual(numbers.numbers, [1,2,3])
    
    def test_user_numbers_with_extra_spaces(self):
        numbers = UserNumbers("1 2   3  ")
        self.assertEqual(numbers.numbers, [1,2,3])
    
    def test_user_numbers_error(self):
        with self.assertRaises(ValueError):
            numbers = UserNumbers("oui oiu")
        
    def test_user_numbers_reversed(self):
        numbers = UserNumbers("1 2   3  ")
        self.assertEqual(numbers.reversed(), [3, 2, 1])

    def test_user_numbers_max(self):
        numbers = UserNumbers("1 2   3  ")
        self.assertEqual(numbers.max(), 3 )     

    def test_user_numbers_min(self):
        numbers = UserNumbers("1 2   3  ")
        self.assertEqual(numbers.min(), 1)

    
if __name__ == '__main__':
    unittest.main()