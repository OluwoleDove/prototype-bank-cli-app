from bankclass import Account, Savings, Current

def bank_mix(user):
    option = input("\nSelect your account type: \n1. New User\n2. Old User\n\n")
    if option == "1":
        my_acc = Account()
    else:
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