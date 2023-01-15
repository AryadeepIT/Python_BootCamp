import os
 
def clear():
    os.system('cls')
 
clear()

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


name_money = {}
 
print(logo)
print("Welcome to the secret auction program.")
 
is_end = True
while is_end==True:
    bidder = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    name_money[bidder] = bid
    print()
    other = input("Are there any other bidders? Type 'yes' or 'no': ")
    if other=="yes":
        clear()
        continue
    elif other=="no":
        clear()
        highest_bidder = max(name_money, key=name_money.get) 
        print(f"The winner is {highest_bidder} with a bid of {name_money[highest_bidder]}")
        break