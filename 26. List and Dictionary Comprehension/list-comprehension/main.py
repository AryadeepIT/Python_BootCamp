numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Aryadeep"
letter_list = [letter for letter in name]
print(letter_list)

range_list = [num*2 for num in range(1, 5)]
print(range_list)

names = ["Arya", "Aryadeep", "Sanchita", "Munu"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

upper_names = [name.upper() for name in names]
print(upper_names)
