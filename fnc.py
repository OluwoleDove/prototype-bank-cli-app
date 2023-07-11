from tnxfunctions import process_transactions, input_prompt

def choose_account():
    option = input("\nSelect your account type: \n1. Savings Account\n2. Current Account\n\n")
    if option == "1":
        this_customer = input_prompt()
        process_transactions(this_customer, "create_account")

    elif option == "2":
        this_customer = input_prompt()
        process_transactions(this_customer, "create_account")

def bank_mix():
    option = input("\nChoose an option: \n1. Visitor\n2. Returning User\n\n")
    if option == "1":
        choose_account()
        new_customer = input_prompt()
        process_transactions(new_customer, "create_account")
    else:
        choose_account()
        


bank_mix()
check = input("Do you want to perform another transaction? Y/N\n")
while check == "Y" or check == "y":
    bank_mix()
    check = input("Do you want to perform another transaction? Y/N\n")

print("\nThanks for banking with us.")