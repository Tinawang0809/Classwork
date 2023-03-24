# from cryptography.fernet import Fernet
# #create the cipher for the password entered by the usercipher_key
# cipher_key = Fernet.generate_key()
# print(cipher_key)
# cipher = Fernet(cipher_key)
# text = b'My name is xxx.'
# #encryption
# encrypted_text = cipher.encrypt(text)
# print(encrypted_text)
# #decypher the encrypted text
# decrypted_text = cipher.decrypt(encrypted_text)
# print(decrypted_text)
import os, random, datetime

class Persistent:
    file = "";
    cache = []
    def __init__(self, filename):
        self.filename = filename

#get password and account
    def getAccount(self, account):
            self.file = open(self.filename, "r")
            lines = self.file.readlines()
            # Strips the newline character
            for line in lines:
                print(line)
                line_list = line.split("\t")
                print(line_list)
     #Based on the file entered, returning to current account's information(password)

     def updateAccount(self, account, password):
        pass
        # Update the current file's account information (Password)

    def createAccount(self, account, password):
        pass
        # Adding the new account/ account's password information into the user file

    def deleteAccount(self, account):
        pass
        # delete the targeted account information entered by the user in the user file

    def listAccount(self):
        pass
        # List and print all the account information in the user file



# main menu
my_perststent = Persistent("db")
while True:
    print("______________  My Password Assistant  ______________")
    print("______________  1) Create account      ______________")
    print("______________  2) Service page        ______________")
    print("______________  3) exit  ***********************")
    cmd = input("Please choose your option: ")
    if cmd == 3 or cmd == '3':
        print("Thanks for you use.")
        exit()




# service menu
    print("####################################")
    print("#         Service Page             #")
    print("#       1 Add Account              #")
    print("#       2 Update Account           #")
    print("#       3 Delete Account           #")
    print("#       4 Display list             #")
    print("#       5 Exit                     #")
    print("########################################")
    choice = input("Enter your choice ")
        os.system('clear')
    if '1' in choice:
        print(" enter a random letter to start guessing the word! If the letter is within the word, it will show you !!!")
        input(" Press return to go back to main menu" )
        Menu()
    elif '6' in choice:
        print ("good Bye")
        exit()
    elif '2' in choice or '3' in choice or '4' in choice:
        selectWord(choice)
    elif '5' in choice:
        print_scoreboard()
        input(" Press return to go back to main menu" )
        Menu()

    else:
        print("PLease enter a valid option")
        Menu()
    if cmd == 0 or cmd == '0':
        print("Thanks for you use.")
        exit()
    elif cmd == 1 or cmd == '1':
        account = input("Please enter your account that your need the password: ")
        #TODO get the password from file
        my_perststent.getAccount(account);
    elif cmd == 2 or cmd == '2':
        account = input("Please enter your account that your need the password: ")
        #TODO 1. Check whether current account exists in the file
        #TODO 3: Can we set the input to '*' while input password ?
        password = input("Please enter your new password for this account.")
        confirmed_password = input("Please enter your new password for this account again.")
        #TODO 2. Create/Update password into current account
        # validate your input !!!
        # check option create new or update ???
        my_perststent.updateAccount(account, password)
        my_perststent.createAccount(account, password)
    elif cmd == 3 or cmd == '3':
        account = input("Please enter your account that your need to delete password: ")
        # TODO 1. Check whether current account exists in the file
        # TODO 2. Delete the account with the password
        my_perststent.deleteAccount(account)
    elif cmd == 4 or cmd == '4':
        pass
        # TODO 1. print("List all accounts: ")
        # TODO 2. print("Search all accounts: ")
        my_perststent.listAccount()
    else:
        print("Your input is invalid, please choose the correct option !!!")
