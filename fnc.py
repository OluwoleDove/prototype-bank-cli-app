from tnxfunctions import process_transactions, input_prompt

def choose_account():
    users_tab = ["firstname", "lastname", "email", "phone", "occupation", "gender", "dob", "city", "joindate"]
    accounts_tab = ["account_type", "balance", "charges", "interests", "pin", "last_edited"]
    transactions_tab = ["transaction_type", "transaction_amount", "transaction_date"]
    acc_type = ""
    option = input("\nSelect your account type: \n1. Savings Account\n2. Current Account\n\n")
    if option == "1":
        acc_type = "Savings"
    elif option == "2":
        acc_type = "Current"
        tnx_type = input("\nSelect transaction type: \n1. Create Account \n2. Change Pin\n3. Check Balance\n4. Deposit\n5. Withdrawal\n6. Transfer\n.9. Edit User Details\n8. Close Account\n\n")
        tnx_dict = {"1":"Create Account", "2":"Change Pin", "3":"Check Balance", "4":"Deposit", "5":"Withdrawal", "6":"Transfer", "7":"Edit User Details", "8":"Close Account"}
    
    this_customer = input_prompt(users_tab)
    process_transactions(this_customer, "change_pin")
        

def bank_mix():
    choose_account()
        


bank_mix()
check = input("Do you want to perform another transaction? Y/N\n")
while check == "Y" or check == "y":
    bank_mix()
    check = input("Do you want to perform another transaction? Y/N\n")

print("\nThanks for banking with us.")