from bank_mix import bank_mix
import tnxfunctions

def main():
    print("A PROTOTYPE BANK CLI APP BUILT WITH PYTHON AND MYSQL\nWelcome to Techcurious Bank PLC\n")
    bank_mix()
    check = input("Do you want to perform another transaction? Y/N\n")
    while check == "Y" or check == "y":
        bank_mix()
        check = input("Do you want to perform another transaction? Y/N\n")

    print("\nThanks for banking with us.")

if __name__ == "__main__":
    main()
