import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items=len(names)
random_choice=random.randint(0,num_items-1)
print(names[random_choice]+" is going to buy the meal today!")