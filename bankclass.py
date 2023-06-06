class Account:
    def __init__(this, name, job, gender, balance, city):
        this.name = name
        this.job = job
        this.balance = balance 
        this.gender = gender
        this.city =  city

    def create_pin(this, user_pin):
        if len(user_pin) > 4:
            return "You pin should be a four digits number please"
        else:
            pass

class Savings(Account):
    def __init__(this, name, job, balance, noy):
        super().__init__(name, job, balance)
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
        
class Current(Account):
    def __init__(this, name, job, balance, noy):
        super().__init__(name, job, balance)
        this.noy = noy

    def show(this):
        print("Your current account balance is " + this.balance)

    def calc_charges(this):
        this.balance -= this.balance * 0.02 * this.noy
        print(("Current account balance for {0} after deducting charges is; {1}").format(this.name, this.balance))
    
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