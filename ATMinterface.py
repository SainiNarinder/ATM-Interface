import time         # time module imported

print("Please enter your CARD ")       

time.sleep(3)        # 3 sec pause                  

password=1234        # setting password
pin=int(input("Enter your pin: "))  # getting pin from user 
balance=5000

if pin==password:      #checking validity of pin 
 while(True):
    print("""
          1 == Balance
          2 == Withdraw
          3 == Deposit
          4 == exit
       """)
    try:
        option=int(input("\nPlease enter your choice: "))  # reading user choice
    except:
        print("Please enter valid option")
        
    if option==1:          # Showing Balance
        print(f"\nYour balance is {balance}")
        
    if option==2:          # withdraw Amount 
        withdraw_amt=int(input("\tEnter the Amount: "))
        balance-=withdraw_amt
        print(f"\n\t\t{withdraw_amt} is debited from account.")
        print(f"\n\t\tCurrent Balance= {balance}")
        
    if option==3:          # Depositing Amount 
        deposit_amt=int(input("\tEnter the Amount: "))
        balance+=deposit_amt
        print(f"\n\t\t{deposit_amt} is credited to your account.")
        print(f"\n\t\tCurrent Balance= {balance}")
        
    if option==4:          # EXIT
        break
    
    
else:                      # wrong pin case
    print("Wrong pin Please try again")
        