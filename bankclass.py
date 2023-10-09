class Account:
    def __init__(this, first_name, last_name, email, phone, gender, dob, occupation, city):
        this.first_name = first_name
        this.last_name = last_name
        this.email = email
        this.phone = phone
        this.gender = gender
        this.dob = dob
        this.occupation = occupation
        this.city =  city
        this.balance = 0.0

    def create_pin(this, user_pin):
        if len(user_pin) > 4:
            return "You pin should be a four digits number please"
        else:
            pass

class Savings(Account):
    def __init__(this, first_name, last_name, email, phone, gender, dob, occupation, city, balance):
        super().__init__(first_name, last_name, email, phone, gender, dob, occupation, city, balance)
        this.noy = 0
        this.balance = balance #comes from database

    def show(this):
        print("Your savings account balance is " + this.balance)
    
    def calc_interest(this):
        this.balance += this.balance * 0.05 * this.noy
        print(("Savings account balance for {0} after adding interest is; {1}").format(this.first_name, this.balance))
    
    def deposit(this, amount):
        this.balance += amount
        return this.balance

    def withdraw(this, amount):
        this.balance += amount
        return this.balance
        
class Current(Account):
    def __init__(this, first_name, last_name, email, phone, gender, dob, occupation, city):
        super().__init__(first_name, last_name, email, phone, gender, dob, occupation, city)
        this.noy = 0

    def show(this):
        print("Your current account balance is " + this.balance)

    def calc_charges(this):
        this.balance -= this.balance * 0.02 * this.noy
        print(("Current account balance for {0} after deducting charges is; {1}").format(this.first_name, this.balance))
    
    def deposit(this, balance, amount):
        this.balance = balance
        this.balance += amount
        return this.balance

    def withdraw(this, balance, amount):
        this.balance = balance
        this.balance += amount
        return this.balance