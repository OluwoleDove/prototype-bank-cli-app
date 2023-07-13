class Account:
    def __init__(this, first_name, last_name, email, phone, gender, dob, occupation, city):
        this.first_name = first_name
        this.last_name = last_name
        this.email = email
        this.phone = phone
        this.occupation = occupation
        this.gender = gender
        this.dob = dob
        this.city =  city
        this.balance = 0

    def create_pin(this, user_pin):
        if len(user_pin) > 4:
            return "You pin should be a four digits number please"
        else:
            pass

class Savings(Account):
    def __init__(this, first_name, last_name, email, phone, gender, dob, occupation, balance, noy):
        super().__init__(first_name, last_name, email, phone, gender, dob, occupation, balance)
        this.noy = noy

    def show(this):
        print("Your savings account balance is " + this.balance)
    
    def calc_interest(this):
        this.balance += this.balance * 0.05 * this.noy
        print(("Savings account balance for {0} after adding interest is; {1}").format(this.first_name, this.balance))
    
    def deposit(this, balance, amount):
        this.balance = balance
        this.balance += amount
        return this.balance

    def withdraw(this, balance, amount):
        this.balance = balance
        this.balance += amount
        return this.balance
        
class Current(Account):
    def __init__(this, first_name, last_name, occupation, balance, noy):
        super().__init__(first_name, last_name, occupation, balance)
        this.noy = noy

    def show(this):
        print("Your current account balance is " + this.balance)

    def calc_charges(this):
        this.balance -= this.balance * 0.02 * this.noy
        print(("Current account balance for {0} after deducting charges is; {1}").format(this.first_name, this.balance))
    
    def deposit(this):
        amount = float(input("Enter the deposit value: "))
        this.balance += amount
        print("Your new savings balance is: " + str(this.balance))

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