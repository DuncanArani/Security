
import pyperclip

class Password:
    # this class generates instance of passwords
    password_list=[] #empty list

    def __init__(self, first_name , last_name,email, password):
        #removed docstring for simplicity

        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password

    def save_password(self):
        # saves password into password list
        Password.password_list.append(self)
        

    def delete_password(self):

        # deleting a saved password

        Password.password_list.remove(self)
        
@classmethod
def find_by_email(cls,email):



            for password in cls.password_list:
                if password.password==password:
                    return password

@classmethod
def password_exist(cls,email):
        # checks if the password exists from the password list
        for password in cls.contact_list:
            if password.password==password:
                return True

        return False

@classmethod
def display_password(cls):

    # returns a password list
    return cls.password_list

@classmethod
def copy_email(cls,email):
    password_found=Password.find_by_email(email)
    pyperclip.copy(password_found.email)

def check_existing_password(email):
    # checks if the password exist with that email and return a booleon
    return Password.password_exist(email)


