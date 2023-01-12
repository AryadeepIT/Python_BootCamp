year = int(input("Which year do you want to check? "))

if year%4 ==0 and year%400==0:
    print(f"Leap year")
elif year % 100 != 0 and year % 4 == 0:
    print("Leap year")
else:
    print(f"Not leap year") 