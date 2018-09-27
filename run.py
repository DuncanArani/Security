#!/usr/bin/env python3.6
from password import Password

# creating new password
def create_password(first_name,last_name, email, password):
    new_password = Password(first_name, last_name, email, password)
    return new_password

def save_passwords(password):
# We create a save_passwords function that takes in a password  object and then calls the save_password method to save the password.
    # funnction that saves the password
    password.save_password() 

def delete_password(password):
    # function that enables one to delete a password    
    password.delete_password()

def find_password(security):

# the function that finds password by email and theen returns password
    return Password.find_by__security(security)



def check_existing_passwords(security):

# function that checks if the password is existing with email amd returns a booleon
    return Password.password_exist(security)

def display_password():

    # function that all saved passwords and displays them
    return Password.display_passwords()


#  the above is the defination of functions

# calling of the functions bellow
def main():
        print("Hello Welcome to your password list. What is your name?")
        user_name = input()

        print(f"Hello {user_name}. what would you like to access?")
        print('\n')

while True:
        print("Use these short codes : cp - create a new password, dp - display passwords, fp -find a password, ex -exit the password list ")

        short_code = input().lower()

        if short_code == 'cp':
                print("New Password")
                print("-"*10)

                print ("First name ")
                first_name = input()

                print("Last name")
                last_name = input()

                print("email")
                email= input()

                print("password")
                password = input()

                save_password(create_password(first_name,last_name,email,password)) 
                print ('\n')
                print(f"New Password {first_name} {last_name} {email} created")
                print ('\n')

        elif short_code == 'dp':

                if display_passwords():
                    print("Here is a list of  your saved passwords")
                    print('\n')
                
                for password in display_passwords():
                    print(f"{password.first_name} {password.last_name}{password.email}")
                    print('\n')
                    
                else:
                    print('\n')
                    print("You  have no passwords saved yet")
                    print('\n')

                                
        elif short_code == 'fp':

            print("Enter the email you want to search password for")

            search_email = input()

            if check_existing_password(search_email):

                search_email = find_password(search_email)
                print(f"{search_password.first_name} {search_password.last_name}")
                print('-' * 20)

                print(f"email{search_password.email}")
                print(f"password{search_password.password}")
            else:
                        print("That password does not exist")

                
        elif short_code == "ex":
                print("thank you")
                break

        else:
                    print("Results not found. Please use the short codes")


    
    
if __name__ == '__main__':
    
    main()

