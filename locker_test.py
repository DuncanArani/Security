import unittest

from locker import Locker

class TestLocker(unittest.TestCase):

    #tearDown function
    def tearDown(self): 
        Locker.locker_list = []

    # test the setUp
    def setUp(self):
        self.new_password = Locker("GitHub","DuncanArani","dunco254")

    # test the initialization
    def test__init__(self):
        self.assertEqual(self.new_password.acc_name,"GitHub")
        self.assertEqual(self.new_password.username,"DuncanArani")
        self.assertEqual(self.new_password.password,"dunco254")

    # ***********  TEST IT'S ABILITIES  ***************

    # ability to save a password 
    def test_save_password(self):
        self.new_password.save_password()
        self.assertEqual(len(Locker.locker_list),1)

    # ability to save multiple passwords
    def test_saving_multiple_passwords(self):
        self.new_password.save_password()

        new_password = Locker("FaceBook","fbUser","fbUser21")
        new_password.save_password()

        self.assertEqual(len(Locker.locker_list),2)

    # ability to delete a password
    def test_delete_password(self):
        self.new_password.save_password()
        new_password = Locker("Test","test","passTest1")
        new_password.save_password()

        new_password.delete_password()

        #test if it has deleted the password
        self.assertEqual(len(Locker.locker_list),1)


    
if __name__ == '__main__':
    unittest.main()
