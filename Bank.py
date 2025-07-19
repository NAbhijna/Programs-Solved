from datetime import datetime
import pytz

def deposit(Accounts, ch):
    amt = int(input("Enter the amount you want to deposit"))
    Accounts[ch] += amt
    print(f"Rs. {amt} deposited in account {ch}")

def withdraw(Accounts, ch):
    while(True):
        amt = int(input("Enter the amount you want to withdraw"))
        if (amt>Accounts[ch]):
            print("Insufficient Balance")
        else:
            Accounts[ch] -= amt
            print("Withdrawal successful")
            break
        
def transfer(Accounts, ch):
    while(True):
        acc = int(input("Enter the account number to transfer to: "))
        if acc in Accounts:
            amt = int(input("Enter the amount to transfer"))
            if amt > Accounts[ch]:
                print("Insufficient balance")
            else:
                Accounts[acc] += amt
                print("Transfer complete")
                break
        else:
            print("Account not found")
        

def menu(Accounts, ch):
    while(True):
        print(f"\n--- Welcome to account {ch} ---")
        print("1. Display\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Logout")
        a = int(input("Enter your choice"))
        match a:
            case 1:
                print(f"Account no. {ch} \t Balance : {Accounts[ch]}")
            case 2:
                deposit(Accounts, ch)
            case 3:
                withdraw(Accounts, ch)
            case 4: 
                transfer(Accounts, ch)
            case 5:
                print("Logging out")
                break           

Accounts = {101: 1000, 102: 1000, 103: 1000}
s = datetime.strptime("1:00", "%H:%M").time()
e = datetime.strptime("1:00", "%H:%M").time()

while(True):
    print("----->> Welcome to banking system <<------")
    now = datetime.now(pytz.timezone('Asia/Kolkata')).time()
    c = now.replace(second=0, microsecond=0)
    if s<= c <= e:
        ch = int(input("Enter the account number (press 0 to exit)"))
        if(ch==0):
            print("Exiting the System")
            exit(0)
        elif(ch not in Accounts):
            print("!!! Account does not exist !!!")
        else:
            menu(Accounts, ch)
    else: 
        print("Maintenance time. Try again later!")
        break