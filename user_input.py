def user_numbers(numbers_string):
    numbers_string
    numbers = numbers_string.split()
    try:
        return [int(n) for n in numbers]
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")

def user_numbers_reversed(numbers):
   result = list(reversed(user_numbers(numbers)))
   return result

# write a test function
# test_user_numbers_max
# which makes sure that 
# user_numbers_max(["1, 2, 3"])
# gives 3 
# and implement this function
def user_numbers_max(numbers_string):   
    return max(user_numbers(numbers_string))


def user_numbers_min(numbers_string):
    return min(user_numbers(numbers_string))

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
        self.assertEqual(user_numbers_reversed("1 2 3"), [3,2,1])

    def test_user_numbers_max(self):
        self.assertEqual(user_numbers_max("1 2 3"), 3 )     

    def test_user_numbers_min(self):
        self.assertEqual(user_numbers_min("1 2 3"), 1)

    def test_user_numbers_min_list(self):
        self.assertEqual(min([1, 2, 3]), 1)


    
if __name__ == '__main__':
    unittest.main()