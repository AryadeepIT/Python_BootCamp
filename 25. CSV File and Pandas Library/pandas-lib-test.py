import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))


# average = sum(temp_list) / len(temp_list)
# print(average)

print(data["temp"].mean())  # average of temp using single line
print(data["temp"].max())  # maximum temp

# print(data["condition"])
print(data.condition)  # same output as above

# Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 +32
print(monday_temp_F)