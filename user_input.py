

def user_numbers(numbers_string):
    numbers_string
    numbers = numbers_string.split()
    result = []
    for n in numbers:
        result.append(int(n))

    return result


import unittest

class TestUserInput(unittest.TestCase):

    def test_user_numbers(self):
        self.assertEqual(user_numbers("1 2 3"), [1,2,3])
    
if __name__ == '__main__':
    unittest.main()