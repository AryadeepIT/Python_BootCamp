with open("file1.txt") as file1:
    file_1 = file1.readlines()

with open("file2.txt") as file2:
    file_2 = file2.readlines()

result = [int(item) for item in file_1 if item in file_2]

print(result)
