
#!/usr/bin/env python3.6
import string
import random
import datetime
from locker import Locker
from user import User


def passwor_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def new_password(account, username, thepass):
    new_pass = Locker(account, username, thepass)
    return new_pass


def save_password(password):
    password.save_password()


def del_password(password):
    password.delete_password()


def display_password(username):
    return Locker.find_by_username(username)


def search_if_exists(username):
    return Locker.password_exists(username)


def display_all():
    return Locker.display_password()

    # ********** USER RELATED FUNCTIONS *********


def check_exists(username):
    return User.user_exists(username)


def new_user(name, username, email, thepass):
    new_user = User(name, username, email, thepass)
    return new_user


def save_new_user(user):
    user.save_user()


def auth(username, password):
    return User.pass_check(username, password)


def it_checks(a, b):
    if a == b:
        return True


time = datetime.datetime.now()


def main():
    print("-"*40)

    print("Welcome to pSecure App ! Sign up to continue")

    print("-"*70)

    while True:
        print("""
            Select an option :
            [1] . Login
            [2] . Sign up
            [3] . Exit App
        """)

        select = input()

        if select == "1":
            print("Enter a username :")
            username = input()

            print("\nEnter your password")

            password = input()

            if check_exists(username):
                if auth(username, password):
                    while True:
                        print("-"*70)
                        print(f"pSecure  | Logged in as {username} | %time.!")
                        print("-"*70)
                        print("""
                            Kindly select an option to proceed :\n
                            [1] . Create a locker \n
                            [2] . Search  \n
                            [3] . Display your locked passwords \n
                            [4] . Delete a password \n 
                            [5] . Logout\n
                            """)

                        choice = input()

                        if choice == "1":
                            print("Store a new Password :")
                            print("-"*70)

                            print("Enter Account e.g Facebook \n")
                            acc = input()
                            print("-"*70)

                            print("Enter username e.g aruncodunco\n")
                            username = input()
                            print("-"*40)

                            print("""You are doing Fantastic !\nNow , would you like us to generate a password for you ?\n
                                    Y or N ?
                                """)

                            yono = input()

                            if yono.lower() == "y":
                                password = passwor_generator()
                            elif yono.lower() == "n":
                                print("Enter your password :")
                                password = input()
                            else:
                                print("\nInput unrecognized !")
                                break

                            save_password(new_password(
                                acc, username, password))

                            print("-"*70)
                            print(f"""New Password locked !\n 
                                Account : {acc}\n
                                Username: {username}\n
                                Password: {password}""")
                            print("-"*70)

                            # search password
                        elif choice == "2":
                            search = input("\nEnter username :\n")

                            if search_if_exists(search):
                                searched = display_password(search)
                                print("-"*70)
                                print("ACCOUNT  |  USERNAME  |  PASSWORD")
                                print("-"*70)
                                print(
                                    f"{searched.acc_name} | {searched.username} | {searched.password}")
                                print("-"*70)
                            else:
                                print("Password not found !")

                            # display all passwords
                        elif choice == "3":
                            print("Here are your passwords :")
                            print("-"*70)
                            print("ACCOUNT  |  USERNAME  |  PASSWORD")

                            if display_all():
                                for locked in display_all():
                                    print("-"*70)
                                    print(
                                        f"{locked.acc_name} | {locked.username} | {locked.password}")
                            else:
                                print("-"*70)
                                print(
                                    "Ooops ! It's lonely here . You haven't locked any password(s)")
                                print("-"*70)

                            # delete specific password
                        elif choice == "4":
                            print("Kindly provide username")
                            which = input()
                            found = display_password(which)

                            if search_if_exists(which):
                                print("Confirm . Y or N")
                                confirm = input()
                                if confirm.lower() == "y":
                                    del_password(found)
                                    print("-"*70)
                                    print("Successfully deleted !")
                                    print("-"*70)
                                elif confirm.lower() == "n":
                                    print("-"*70)
                                    print("Permission Denied !")
                                    print("-"*70)
                                else:
                                    print("Sorry I didn't get that !")
                            else:
                                print("-"*70)
                                print(
                                    "\nRecord not found ! Add Passwords to your locker .\n")
                                print("-"*70)

                            # exit the application
                        elif choice == "5":
                            print("-"*70)
                            print("Logged Out !")
                            print("-"*70)
                            break

                        else:
                            print(
                                "I'm sorry I didn't get that . Kindly use the provided option . ")
                else:
                    print("-"*70)
                    print("Sorry ! Couldn't match your credentials !")

            else:
                print("-"*70)
                print("\nKindly Sign Up to use pSecure !")

        elif select == "2":
            # print("Enter First Name and Last Name :")
            print("-"*70)
            f_and_last = input("Enter your First Name and Last Name :")

            # print("Choose a username :")
            print("-"*70)
            u_name = input("Choose a username : ")

            # print("Enter email :")
            print("-"*70)
            email = input("Enter email :")

            print("-"*70)
            initial = input("Enter password :")
            # initial = input()
            # print("Repeat password :")
            print("-"*70)
            repeated = input("Repeat password :")

            if it_checks(initial, repeated):
                save_new_user(new_user(f_and_last, u_name, email, initial))

                print("-"*70)
                print(
                    f"Welcome aboard {u_name} ! Login to secure some password !")
                print("-"*70)
            else:
                print("-"*70)
                print("""Ooops ! password didn't check !""")
                print("-"*70)

        elif select == "3":
            print("-"*70)
            print("Thanks for using pSecure . Bye ! .....")
            print("-"*70)
            break

        else:
            print("-"*70)
            print("Am sorry I didn't get that !")


if __name__ == '__main__':

    main()
