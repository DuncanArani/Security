class Locker:
    locker_list = []

    def __init__(self , acc_name , username , password ):
        self.acc_name = acc_name
        self.username = username
        self.password = password

        #  *** save passwords *** #
    def save_password(self):
        Locker.locker_list.append(self)
    
        #  *** delete a password *** #
    def delete_password(self):
        Locker.locker_list.remove(self)
    

        #  *** finding a password *** #
    @classmethod 
    def find_by_username(cls,username):
        for item in Locker.locker_list:
            if item.username == username:
                return item

         #  *** displaying all locked password *** #
    @classmethod 
    def display_password(cls):
        return Locker.locker_list

        #  *** password exists in our list *** #
    @classmethod 
    def password_exists(cls,username):
        for item in Locker.locker_list:
            if item.username == username:
                return True
