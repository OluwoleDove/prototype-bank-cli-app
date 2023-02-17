class Account:
    def __init__(this, name, bank, balance):
        this.name = name
        this.bank = bank
        this.balance = balance 

class Savings(Account):
    def __init__(this, name, bank, balance, noy):
        super().__init__(name, bank, balance)
        this.noy = noy

    def show(this):
        print("Your savings account balance is " + this.balance)
    
    def calc_interest(this):
        this.balance += this.balance * 0.05 * this.noy
        print(("Savings account balance for {0} after adding interest is; {1}").format(this.name, this.balance))
    
    def deposit(this):
        amount = float(input("Enter the deposit value: "))
        this.balance += amount
        print("Your new savings balance is: " + str(this.balance))
        

class Current(Account):
    def __init__(this, name, bank, balance, noy):
        super().__init__(name, bank, balance)
        this.noy = noy

    def show(this):
        print("Your current account balance is " + this.balance)

    def calc_charges(this):
        this.balance -= this.balance * 0.02 * this.noy
        print(("Current account balance for {0} after deducting charges is; {1}").format(this.name, this.balance))
    
    def withdraw(this):
        try:
            amount = float(input("Enter the withdrawal amount: "))
            if amount > this.balance:
                # raise the ValueError
                raise ValueError("Insufficient Funds")
            else:
                this.balance -= amount
                print("Your new current balance is: " + str(this.balance))
        # if false then raise the value error
        except ValueError as e:
                print(e)
                print("Please supply a floating value for the amount")

def bank_mix(user):
    option = input("\nSelect your account type: \n1. Savings Account\n2. Current Account\n\n")
    if option == "1":
        print(("Welcome to {0}").format(user_input[1]))
        my_acc = Savings(user_input[0], user_input[1], float(user_input[2]), 5)
        my_acc.show
        my_acc.deposit()
        my_acc.calc_interest()
        print()
    elif option == "2":
        print(("Welcome to {0}").format(user_input[1]))
        my_acc = Current(user_input[0], user_input[1], float(user_input[2]), 5)
        my_acc.show
        my_acc.withdraw()
        my_acc.calc_charges()
    else:
        bank_mix(user)
    print()

print("THIS PROGRAM MIMICS BANK TRANSACTIONS")
user_input = []
user_input.append(input("Enter customer's name: "))
user_input.append(input("Enter bank name: "))
user_input.append(50000)

bank_mix(user_input)
check = input("Do you want to perform another transaction? Y/N\n")
while check == "Y" or check == "y":
    bank_mix(user_input)
    check = input("Do you want to perform another transaction? Y/N\n")

print("\nThanks for banking with us.")