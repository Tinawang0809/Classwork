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
import os

class Persistent:
    def __init__(self) -> None:
       self._file_name="my.db"
       self._data={}
       if os.path.exists(self._file_name):
        self._load_data()
       else:
        with open(self._file_name,'w+') as f:
            pass
#independent user files that records each user's own account and password data

    def _save_data(self):
        with open(self._file_name, 'w+') as f:
            for key,value in self._data.items():
                f.write(key+"@#$@#$"+value+"\n")
        print("Save the dict into file successfully .............")
# encryption of the user's password in the file

    def _load_data(self):
        self._data={};
        with open(self._file_name, 'r+') as f:
            for line in f.readlines():
                line_list=line.split("@#$@#$")
                self._data[line_list[0]]=line_list[1]

    # def __del__(self):
    #     self._save_data()

    def get(self, key):
        return self._data.get(key)

    def set(self, key, value):
        self._data[key]=value

    def flush(self):
        self._save_data()

    def existAccount(self, account):
        return self._data.get(account) != None

    def getAccount(self, account):
        return self._data.get(account)

    def updateAccount(self, account, password):
        self._data[account]=password
        self.flush()

    def createAccount(self, account, password):
        self._data[account]=password
        self.flush()

    def deleteAccount(self, account):
        del self._data[account]
        self.flush()

    def listAccount(self):
        return list(self._data.keys())

my_perststent = Persistent()
while True:
    print("-----------------------    My Password Assistant  -----------------------")
    print("-----------------------  1) Access password       -----------------------")
    print("-----------------------  2) Update your password  -----------------------")
    print("-----------------------  3) Delete your password  -----------------------")
    print("-----------------------  4) Print account list    -----------------------")
    print("-----------------------  0) Exit                  -----------------------")
    cmd = input("Please choose your option: ")
    if cmd == 0 or cmd == '0':
        print("Thanks for using.")
        exit()
    elif cmd == 1 or cmd == '1':
        account = input("Please enter your account: ")
        #TODO get the password from file
        if my_perststent.existAccount(account):
            print("You password for this account is: " + str(my_perststent.getAccount(account)));
        else:
            print("The accout your input is not exist in this system")

    elif cmd == 2 or cmd == '2':
        account = input("Please enter your account: ")
        if my_perststent.existAccount(account):
            print("Would you like to update the password? ")
            password="0"
            confirmed_password="1"
            while password != confirmed_password:
                password = maskpass.askpass(prompt="Password:",mask="*")
                confirmed_password = maskpass.askpass(prompt="Confirm Password:",mask="*")
                # input("Please enter your new password for this account.")
                # confirmed_password = input("Please enter your new password for this account again.")
                if password != confirmed_password:
                    print("The entered passworded does not match, please try again")
            my_perststent.updateAccount(account, password)
            print("Password updated successfully...")
        else:
            print("Create a new account: ")
            password="0"
            confirmed_password="1"
            while password != confirmed_password:
                password = maskpass.askpass(prompt="Password:",mask="*")
                confirmed_password = maskpass.askpass(prompt="Confirm Password:",mask="*")
                # password = input("Please enter your new password for this account.")
                # confirmed_password = input("Please enter your new password for this account again.")
                if password != confirmed_password:
                    print("The password your input is not match in twice, please input again")
            my_perststent.createAccount(account, password)
            print("Password created successfully..")

    elif cmd == 3 or cmd == '3':
        account = input("Enter your account: ")
        if my_perststent.existAccount(account):
            my_perststent.deleteAccount(account)
            print("Your account deleted successfully.")
        else:
            print("Your input account is not exist in the system and no need to delete.")
    elif cmd == 4 or cmd == '4':
        print("List all accounts as below: ")
        account_list = my_perststent.listAccount()
        for account in account_list:
            print(account)
    else:
        print("Your input is invalid, please choose the correct option !!!")
