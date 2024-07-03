def user_numbers(numbers_string):
    numbers_string
    numbers = numbers_string.split()
    try:
        return [int(n) for n in numbers]
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")

import unittest

#main unittest class
class TestUserInput(unittest.TestCase):

    def test_user_numbers(self):                            
        self.assertEqual(user_numbers("1 2 3"), [1,2,3])
    
    def test_user_numbers_with_extra_spaces(self):                            
        self.assertEqual(user_numbers("1  2  3"), [1,2,3])
    
    def test_user_numbers_error(self):
        with self.assertRaises(ValueError):
            user_numbers("oiu oui")
    
    def test_user_numbers_error_no_with(self):
        self.assertRaises(ValueError, user_numbers, "oiu oui")
    
if __name__ == '__main__':
    unittest.main()