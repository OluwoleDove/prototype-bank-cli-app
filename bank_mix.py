from receive_inputs import input_prompt
from tnx_func import process_transactions

def bank_mix():
    
    else:
        print("Wrong entry! Please try again.")
        bank_mix()
    
    tnx_type = input("\nSelect transaction type: \n1. Create Account \n2. Change Pin\n3. Check Balance\n4. Deposit\n5. Withdrawal\n6. Transfer\n7. Close Account\n\n")
    tnx_dict = {"1":"create_account", "2":"change_pin", "3":"check_balance", "4":"deposit", "5":"withdrawal", "6":"funds_transfer", "7":"close_account"}
    
    if isinstance(int(tnx_type), int):   
        this_customer = input_prompt(tnx_dict[tnx_type])
    else:
        print("Only numerical entry please! Try again.")
        bank_mix()

    process_transactions(this_customer, acc_type, tnx_dict[tnx_type])