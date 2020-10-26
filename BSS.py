from random import randint
'''
Simulate a Banking System (OOPs Project) ......
'''

class Bank:
    def __init__(self):
        self.account = {}

    def Create_Account(self, name, intital_deposit):
        self.account_number = randint(10000,99999)
        self.account[self.account_number] = [name, initial_deposit]
        print("Account Creation is Succesful. Your Account Number is", self.account_number)
        print("\n")

    def authenticate(self, name, account_number):
        if account_number in self.account.keys():
            if self.account[account_number][0] == name:
                self.account_number = account_number
                print("Authentication Successful")
                print("\n")
                return True
            else:
                print("Authentication Unsuccessful")
                print("\n")
                return False
        else:
            print("Authentication Unsuccessful")
            print("\n")
            return False

    def withdraw(self,withdrawal_amount):
        if withdrawal_amount > self.account[self.account_number][1]:
            print("Insufficient Balance")
            print("\n")
        else:
            self.account[self.account_number][1] -= withdrawal_amount
            print("Withdrawal Successful")
            self.display()

    def deposit(self,deposit_amount):
        self.account[self.account_number][1] += deposit_amount
        print("Amount Deposition Successful")
        self.display()

    def display(self):
        print("Available Balance: ", self.account[self.account_number][1])
        print("\n")

Account = Bank()
while True:
    print("Welcome to ABC Bank!!")
    print("Enter 1 to create an account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit the bank")
    user_choice = int(input())
    if user_choice == 1:
        print("Enter account holder name:")
        name = input()
        print("Intial Deposit:")
        initial_deposit = int(input())
        Account.Create_Account(name,initial_deposit)
    elif user_choice == 2:
        print("Enter your name")
        name = input()
        print("Enter your Account Number")
        account_number = int(input())
        authentication_status = Account.authenticate(name, account_number)
        if authentication_status is True:
            while True:
                print("Enter 1 for withdraw")
                print("Enter 2 for deposit")
                print("Enter 3 to display balance")
                print("Enter 4 to go to back menu")
                choice = int(input())
                if choice == 1:
                    print("Enter amount to withdraw")
                    amt = int(input())
                    Account.withdraw(amt)
                elif choice == 2:
                    print("Enter amount to deposit")
                    amt = int(input())
                    Account.deposit(amt)
                elif choice == 3:
                    Account.display()
                else:
                    break
    elif user_choice == 3:
        print("Thankyou!!")
        break
    else:
        print("Please Enter correct key")
        continue

