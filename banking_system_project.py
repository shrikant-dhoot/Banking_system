import os
import json

class account :
    def __init__(self,account_holder,account_number,blance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.blance = blance

    def debit(self,amount):
        self.amount = amount
        self.blance += amount
        print(f"{self.amount} $ is debit  {self.account_holder}  {"\n"} blance  {self.check_blance()} $")


    def credit(self,amount):
        self.amount = amount
        self.blance -= amount
        print(f"{self.amount} $ is credit  {self.account_holder} {"\n"} blance  {self.check_blance()} $")
        


    def check_blance(self):
        return self.blance 
    

    def user_dict (self):
    # its useful for storing data in josn file
         return {
             
             "account_holder" : self.account_holder,
             "account_number" : self.account_number,
             "blance"         : self.blance

     }
    
user = None  # Initialize user variable to None
users = {} # empty dictionary to store users 

FILE = "user.json" # file for stor data 

if os.path.exists(FILE):
        with open (FILE,"r") as f:
            data = json.load(f)
            for key,value in data.items():
                users[int(key)]=account(value["account_holder"],
                int(value["account_number"]),
                value["blance"])

def save_user():

    user_data={key:value.user_dict() for key,value in users.items() } 
 
    with open (FILE,"w") as f:
        json.dump(user_data,f,indent=4)


while True : 
    print("_" * 25)
    print("====SHRIKANT'S BANK=====")
   
   
    print(" 1.creat new account \n 2.debit \n 3.credit \n 4.chack blance \n 5.exit ")
    
    choice=int(input("enter your choice : "))

    if choice == 1 :
        name = input("enter your name : ")
        accunt_number = int(input("creat your account number : "))

        if accunt_number in users :
            print("account number is already exists ! ")
            continue
        else :
            blance=float(input("enter initial blance : "))

        users[accunt_number]=account(name,accunt_number,blance)
        print(f"account created successfully {name} with blance {blance} $")
        save_user()


    elif choice in [2,3,4]:
        accunt_number = int(input("enter account number : "))   
        
        if accunt_number not in users:
            print("Account not found !")
            continue

        user=users[accunt_number] # for particular user 

    if choice == 2: 
        amt=int(input("enter your amount to debit : "))
        user.debit(amt)
        save_user()


    elif choice == 3: 
        amt=int(input("enter your amount to credit : "))
        user.credit(amt)   
        save_user()

    elif choice == 4 :
        print(user.check_blance())

    elif choice == 5 :
        print("exiting.... \n \n \n ")
        print("Develop by => shrikant...\n \n \n ")
        break
    else :
        print("_" * 25)

        


