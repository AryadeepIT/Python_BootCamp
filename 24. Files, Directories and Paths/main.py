# to read the content of the file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# to write something in the file
with open("my_file.txt", mode="w") as file:
    file.write("\nNew text.")

# append text to the previous text
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# creation of new file only in write mode
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")

