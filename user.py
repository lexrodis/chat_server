import uuid


class ChatUser:
    def __init__(self, user_name = "anonymous") -> None:
        self.id = uuid.uuid4()
        self.user_name = user_name
        
    def get_uuid(self):
        return str(self.id)
    

    def send_message(self, message):
        print(f'{self.user_name}:\n    {message}\n')
        
    


import unittest

class TestUserInput(unittest.TestCase):
    def test_get_uuid(self):
        user = ChatUser("Ronaldo")
        self.assertTrue(isinstance(user.get_uuid(), str))

    def test_default_user_name(self):
        user = ChatUser()
        self.assertEquals(user.user_name, "anonymous")

    