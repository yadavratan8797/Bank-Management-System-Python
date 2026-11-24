# Bank management project.
import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []
    try:
        if Path(database).exists():

            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exists")
    except Exception as err:
        print(f"an Exception occured as {err}")
    @staticmethod
    def update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits, k = 3)
        spchar = random.choices("!@@##$%^&",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def createaccount(self):
        info = {
            "name" : input("tell your name :-"),
            "age" : int(input("tell your age :- ")),
            "email" : input("tell your email :- "),
            "pin" : int(input("tell your pin :- ")),
            "account_No." : Bank.__accountgenerate(),
            "balance" : 0 
        }
        if info['age'] < 18:
            print("sorry you can not create your account")
        else:
            print("account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")
            Bank.data.append(info)
            Bank.update()

    def depositmoney(self):
        account_number = input("please tell your account number ")
        pin = int(input("please tell your pin as well "))
        userdata = [i for i in Bank.data if i ['accountNo.'] == account_number and i['pin'] == pin]

        if userdata == False:
            print("soory no data found")
        else:
            amount = int(input("how much you want to depoit "))
            if amount > 10000 or amount < 0:
                print("sorry the amount is too much you can deposit below 10000")
            else:
                print(userdata)
                userdata[0]['balance'] += amount
                Bank.update()
                print("amount deposited successfully ")


user = Bank()

print("press 1 for creating an account")
print("press 2 for Depositing money in the bank")
print("press 3 for withdrawing the money ")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response:-"))
if check == 1:
    user.createaccount()
if check == 2:
    user.depositmoney() 