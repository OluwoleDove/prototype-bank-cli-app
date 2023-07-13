from tnxfunctions import process_transactions, input_prompt

def choose_account(accounts_arg):
    option = input("\nSelect your account type: \n1. Savings Account\n2. Current Account\n\n")
    if option == "1":
        tnx_type = input("\nSelect transaction type: \n1. Change Pin\n2. Deposit\n3. Withdrawal\n4. Transfer\n5. Close Account\n\n")
        if tnx_type == "1":
            this_customer = input_prompt(accounts_arg)
            process_transactions(this_customer, "change_pin")
    elif option == "2":
        pass
        

def bank_mix():
    users_tab = ["firstname", "lastname", "email", "phone", "occupation", "gender", "dob", "city", "joindate"]
    accounts_tab = ["account_type", "balance", "charges", "interests", "pin", "last_edited"]
    transactions_tab = ["transaction_type", "transaction_amount", "transaction_date"]
    
    option = input("\nChoose an option: \n1. Visitor\n2. Returning User\n\n")
    if option == "1":
        choose_account()
        new_customer = input_prompt(users_tab)
        process_transactions(new_customer, "create_account")
    else:
        choose_account(accounts_tab)
        


bank_mix()
check = input("Do you want to perform another transaction? Y/N\n")
while check == "Y" or check == "y":
    bank_mix()
    check = input("Do you want to perform another transaction? Y/N\n")

print("\nThanks for banking with us.")