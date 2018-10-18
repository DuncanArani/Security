class User:
    users = []

    def __init__(self,f_and_sname,username,email , password):
        self.f_and_sname = f_and_sname
        self.username = username
        self.email = email
        self.password = password
    
    def save_user(self):
        return User.users.append(self)
    
    @classmethod
    def find_user(cls,username):
        for user in User.users:
            if user.username == username:
                return user
        
    @classmethod
    def user_exists(cls,username):
        for user in User.users:
            if user.username == username:
                return True

    @classmethod 
    def pass_check(cls,username,password):
        for user in User.users:
            if user.username == username and user.password == password:
                return True