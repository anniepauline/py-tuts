# Python banking program
balance = 100
is_running = 1
def show_balance():
    print("---------------------------")
    print(f"Your balance is {balance}")
    print("---------------------------")


def withdraw(amount):
    global balance 
    balance -= amount

def deposit(amount):
    global balance
    balance += amount


def banking():
    global is_running
    print("1.Show balance")
    print("2.Withdraw")
    print("3.Deposit")
    print("4.Quit")
    print("---------------------------")
    choice = int(input("Enter you option number: "))
    match choice:
        case 1: 
            show_balance()
        case 2:
            amt = int(input("Enter the amount to withdraw: "))
            if amt < 0:
                print("Amount shd be > 0")
            elif int(amt > balance):
                print("Infussicient funds")
            withdraw(amt)
        case 3:
            amt = int(input("Enter the amount to desposit: "))
            if amt < 0:
                print("AMount shd be > 0")
            deposit(amt)
        case 4:
            print("Exiting program...")
            is_running=0
            return 
        case _:
            print("Invalid option")

while is_running == 1: 
    banking()               
    if is_running == 0:
        break

