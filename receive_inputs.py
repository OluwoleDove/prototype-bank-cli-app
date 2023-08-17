import sys

def get_input():
    for user_input in sys.stdin:
        if 'q' == user_input.rstrip():
            break
        return user_input
        #print(f'Input : {line}')

def input_prompt(client_choice):
    if client_choice == "create_account":
        new_client_tab = ["firstname", "lastname", "email", "phone", "occupation", "gender", "dob", "city", "account_type"]
        input_dict = {}
        print("Getting user input ... Please carefully supply the following")
        for param in new_client_tab:
            print(f"{param}: ")
            input_dict.update({ param : get_input() })

    print(input_dict)
    return input_dict