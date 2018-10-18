import unittest

from user import User

class TestUser(unittest.TestCase):
    def tearDown(self):
        User.users = []

    def setUp(self):
        self.new_user = User("Duncan Arani","duncoarunco","aruncodunco@gmail.com","31740141")
    
    def test__init__(self):
        self.assertEqual(self.new_user.f_and_sname,"Duncan Arani")
        self.assertEqual(self.new_user.username,"duncoarunco")
        self.assertEqual(self.new_user.email,"aruncodunco@gmail.com")
        self.assertEqual(self.new_user.password,"31740141")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users),1)

    def test_saving_users(self):
        self.new_user.save_user()

        new_user = User("dun","gmail","dun@gmail.com","dun254")
        new_user.save_user()

        self.assertEqual(len(User.users),2)


if __name__ == "__main__":
    unittest.main()
