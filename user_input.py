def user_numbers(numbers_string):
    numbers_string
    numbers = numbers_string.split()
    return [int(n) for n in numbers]


import unittest

class TestUserInput(unittest.TestCase):

    def test_user_numbers(self):
        self.assertEqual(user_numbers("1 2 3"), [1,2,3])

def test_user_input_error(self):
    self.assertRaises(ValueError, user_input("oiu oiu"))


    
if __name__ == '__main__':
    unittest.main()