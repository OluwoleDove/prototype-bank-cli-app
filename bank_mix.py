from tnxfunctions import process_transactions, input_prompt

def bank_mix():
    users_tab = ["firstname", "lastname", "email", "phone", "occupation", "gender", "dob", "city", "joindate"]
    accounts_tab = ["account_type", "account_number", "balance", "charges", "interests", "pin", "last_edited"]
    transactions_tab = ["transaction_type", "transaction_amount", "transaction_date"]
    acc_type = ""
    option = input("\nSelect your account type: \n1. Savings Account\n2. Current Account\n\n")
    if option == "1":
        acc_type = "Savings"
    elif option == "2":
        acc_type = "Current"
    
    tnx_type = input("\nSelect transaction type: \n1. Create Account \n2. Change Pin\n3. Check Balance\n4. Deposit\n5. Withdrawal\n6. Transfer\n7. Close Account\n\n")
    tnx_dict = {"1":"create_account", "2":"change_pin", "3":"check_balance", "4":"deposit", "5":"withdrawal", "6":"funds_transfer", "7":"close_account"}
    
    this_customer = input_prompt(users_tab)
    process_transactions(this_customer, acc_type, tnx_dict[tnx_type])