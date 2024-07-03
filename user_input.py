def user_numbers(numbers_string):
    numbers_string
    numbers = numbers_string.split()
    try:
        return [int(n) for n in numbers]
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")

# write a test function which makes sure that 
# user_numbers_reversed(["1", "2", "3"])
# gives ["3", "2, "1"] 
# and implement ths function



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

    def test_user_numbers_reversed(self):
        self.assertEqual(user_numbers("1 2 3"), [3,2,1])     
    
if __name__ == '__main__':
    unittest.main()