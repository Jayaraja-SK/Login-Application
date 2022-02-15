import os
import sys
import hashlib
import string
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from time import sleep
from getpass import getpass


cred = credentials.Certificate("python-eb137-firebase-adminsdk-f1mnw-0d30af0091.json")
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL':"https://python-eb137-default-rtdb.firebaseio.com/"
	})
ref = db.reference("/")


def user_availability(email_id): # TO CHECK IF E-MAIL ID ALREADY EXISTS OR NOT
    sql=ref.get() # RETRIEVE RECORDS

    for key,value in sql.items():
        
        if(type(value)==dict and "Email" in list(value.keys()) and value["Email"]==email_id):
            return True

    return False



def generate_salt_pwd(pwd): # TO GENERATE SALT AND KEY IN HEXA-DECIMAL FORMAT, WHICH IS STORED IN THE DATABASE
    salt=os.urandom(32)

    key=hashlib.pbkdf2_hmac(
        'sha256',
        pwd.encode('utf-8'),
        salt,
        100000
    )

    return salt.hex(),key.hex()



def add_user(email_id,pwd): # ADDING NEW USER'S INFORMATION TO THE DATABASE
    salt,pwd=generate_salt_pwd(pwd) # ADD NEW RECORDS

    temp={"Email":email_id,"Salt":salt,"Password":pwd}

    ref.push().set(temp)



def strong_password(pwd):
    if(len(pwd)<8 and len(pwd)>15):
        return False

    alph_lower=string.ascii_lowercase
    alph_upper=string.ascii_uppercase
    nums=string.digits
    special_chars=["*","@","#","!","&"]

    flag1=0
    flag2=0
    flag3=0
    flag4=0

    for i in pwd:
        if(i in alph_lower):
            flag1=1
        if(i in alph_upper):
            flag2=1
        if(i in nums):
            flag3=1
        if(i in special_chars):
            flag4=1

    if(flag1==0 or flag2==0 or flag3==0 or flag4==0):
        return False

    return True
    


def new_user():
    os.system("cls")
    
    print("-"*50)
    print("\t\tNEW USER CREATION")
    print("-"*50)
    print()
        
    email_id=input("ENTER E-MAIL ID = ")

    if(user_availability(email_id)):
        print("\n\n*** ALERT : E-MAIL ID ALREADY EXISTS ***")
        sleep(5)
        return
    else:
        count=0
        
        while(True):
            if(count>0):
                print("-"*50)
                print("\t\tNEW USER CREATION")
                print("-"*50)
                print()

                print(f'E-MAIL ID = {email_id}')

            print()
            print("-"*60)
            print("\tPASSWORD SHOULD SATISFY THE FOLLOWING")
            print("-"*60)
            print("| 1. | ATLEAST 8 CHARACTERS AND ATMOST 15 CHARACTERS")
            print("| 2. | ATLEAST ONE UPPER-CASE LETTER")
            print("| 3. | ATLEAST ONE LOWER-CASE LETTER")
            print("| 4. | ATLEAST ONE DIGIT")
            print("| 5. | ATLEAST ONE SPECIAL CHARACTER - !, @, #. *, &")
            print("-"*60)
            print()
                
            print()
            pwd=getpass("ENTER PASSWORD = ")
            print()
            confirm_pwd=getpass("CONFIRM PASSWORD = ")
            print()

            count=count+1

            if(pwd==confirm_pwd and strong_password(pwd)):
                break
            elif(pwd==confirm_pwd and strong_password(pwd) is False):
                print("\n\n*** ALERT : PASSWORD IS WEAK, KINDLY ENTER A NEW PASSWORD ***")
                sleep(5)
                
                os.system("cls")
            else:
                print("\n\n*** ALERT : BOTH THE PASSWORDS ARE NOT MATCHING. KINDLY RE-ENTER ***")
                sleep(5)
                
                os.system("cls")

        add_user(email_id,pwd)
        print("\n\n*** ACCOUNT IS CREATED SUCCESSFULLY ... ***")
        sleep(5)
        


def retrieve_salt_pwd(email_id): # TO RETRIEVE SALT AND PASSWORD OF AN EXISTING USER FROM DATABASE
    sql=ref.get()

    for key,value in sql.items():
        if(type(value)==dict and "Email" in list(value.keys()) and value["Email"]==email_id):
            return value["Salt"],value["Password"]
        


def generate_key(salt,pwd): # GENERATE A KEY FOR THE EXISTING SALT AND RECEIVED PASSWORD
    salt=bytes.fromhex(salt)
    
    key=hashlib.pbkdf2_hmac(
        'sha256',
        pwd.encode('utf-8'),
        salt,
        100000
    )

    return key.hex()
    


def pwd_matching(email_id,pwd):
    salt,existing_pwd=retrieve_salt_pwd(email_id)

    new_key=generate_key(salt,pwd)

    if(new_key==existing_pwd):
        return True

    return False



def update_pwd_db(email_id,pwd):
    salt,pwd=generate_salt_pwd(pwd) # UPDATING DATABASE

    sql=ref.get()

    for key,value in sql.items():
        if(type(value)==dict and "Email" in list(value.keys()) and value["Email"]==email_id):
            ref.child(key).update({"Salt":salt,"Password":pwd})




def change_password(email_id):
    os.system("cls")

    print("-"*50)
    print("\t\tCHANGE PASSWORD")
    print("-"*50)
    print(f'EMAIL-ID = {email_id}')
    print()

    count=0
        
    while(True):
        if(count>0):
            os.system("cls")
            
            print("-"*50)
            print("\t\tCHANGE PASSWORD")
            print("-"*50)
            print(f'EMAIL-ID = {email_id}')
            print()

        pwd=getpass("ENTER CURRENT PASSWORD = ")
        print()

        count=count+1

        if(pwd_matching(email_id,pwd)):
            new_pwd=getpass("ENTER NEW PASSWORD = ")
            print()
            confirm_new_pwd=getpass("CONFIRM NEW PASSWORD = ")
            print()

            if(new_pwd==confirm_new_pwd and strong_password(new_pwd)):
                break
            elif(new_pwd==confirm_new_pwd and strong_password(new_pwd) is False):
                print("\n\n*** ALERT : PASSWORD IS WEAK, KINDLY ENTER A NEW PASSWORD ***")
                sleep(5)
            else:
                print("\n\n*** ALERT : NEW PASSWORDS ARE NOT MATCHING. KINDLY RE-ENTER ***")
                sleep(5)
        elif(count>5):
            print("\n\n*** ALERT : MORE THAN 5 FAILED ATTEMPTS. PLEASE TRY AFTER SOMETIME. ***")
            sleep(5)
            return
        else:
            print("\n\n*** ALERT : IN-CORRECT PASSWORD. KINDLY RE-ENTER ***")
            sleep(5)

    update_pwd_db(email_id,new_pwd)
    print("\n\n*** PASSWORD IS CHANGED SUCCESSFULLY ... ***")
    sleep(5)



def delete_info_db(email_id):
    sql=ref.get()

    for key,value in sql.items():
        if(type(value)==dict and "Email" in list(value.keys()) and value["Email"]==email_id):
            ref.child(key).set({}) 



def delete_account(email_id):
    os.system("cls")

    print("-"*50)
    print("\t\tDELETE ACCOUNT")
    print("-"*50)
    print(f'EMAIL-ID = {email_id}')
    print()

    count=0
        
    while(True):
        if(count>0):
            os.system("cls")
            
            print("-"*50)
            print("\t\tDELETE ACCOUNT")
            print("-"*50)
            print(f'EMAIL-ID = {email_id}')
            print()

        pwd=getpass("ENTER PASSWORD = ")
        print()

        count=count+1

        if(pwd_matching(email_id,pwd)):
            delete_info_db(email_id)
            break
        elif(count>5):
            print("\n\n*** ALERT : MORE THAN 5 FAILED ATTEMPTS. PLEASE TRY AFTER SOMETIME. ***")
            sleep(5)
            return 0
        else:
            print("\n\n*** ALERT : IN-CORRECT PASSWORD. KINDLY RE-ENTER ***")
            sleep(5)

    print("\n\n*** ACCOUNT IS DELETED SUCCESSFULLY ... ***")
    sleep(5)

    return 1
            



def dashboard(email_id):
    while(True):
        os.system("cls")
        
        print("-"*50)
        print("\t\tDASHBOARD")
        print("-"*50)
        print(f'EMAIL-ID = {email_id}')
        print("-"*50)
        print(f'1. CHANGE PASSWORD')
        print(f'2. DELETE ACCOUNT')
        print(f'3. LOGOUT')
        print("-"*50)
        print()
        
        choice=int(input("ENTER CHOICE = "))

        if(choice==1):
            change_password(email_id)
        elif(choice==2):
            status=delete_account(email_id)

            if(status==1):
                break
        elif(choice==3):
            print("\n\n*** LOGGING OUT... ***")
            sleep(5)
            return 
    


def existing_user():
    os.system("cls")
    
    print("-"*50)
    print("\t\tEXISTING USER LOGIN")
    print("-"*50)
    print()
        
    email_id=input("ENTER E-MAIL ID = ")

    if(user_availability(email_id) is False):
        print("\n\n*** ALERT : E-MAIL ID DOES NOT EXIST ***")
        sleep(5)
    else:
        count=0
        
        while(True):
            if(count>0):
                print("-"*50)
                print("\t\tEXISTING USER LOGIN")
                print("-"*50)
                print()

                print(f'E-MAIL ID = {email_id}')
                
            print()
            pwd=getpass("ENTER PASSWORD = ")
            print()

            count=count+1

            if(pwd_matching(email_id,pwd)):
                break
            elif(count>=5):
                print("\n\n*** ALERT : MORE THAN 5 FAILED ATTEMPTS. PLEASE TRY AFTER SOMETIME. ***")
                sleep(5)

                return
            else:
                print("\n\n*** ALERT : PASSWORD IS NOT MATCHING. KINDLY RE-ENTER ***")
                sleep(5)

                os.system("cls")
                


        print("\n\n*** LOGIN IS SUCCESSFUL... ***")
        sleep(5)
        dashboard(email_id)
        


def login():
    
    while(True):
        os.system("cls")
        
        print("-"*50)
        print("\tWELCOME TO PYTHON-IDLE LOGIN")
        print("-"*50)
        print(f'1. NEW USER')
        print(f'2. EXISTING USER')
        print(f'3. EXIT')
        print("-"*50)
        print()
        
        choice=int(input("ENTER CHOICE = "))

        if(choice==1):
            new_user()
        elif(choice==2):
            existing_user()
        elif(choice==3):
            sys.exit()


if __name__=="__main__":
    login()
