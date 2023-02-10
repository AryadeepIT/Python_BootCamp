import pandas

student_dict = {
    "student": ["Aryadeep", "Sanchita", "Arya"],
    "score": [56, 76, 55]
}

# # looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)



student_dataframe = pandas.DataFrame(student_dict)
print((student_dataframe))


# # Loop through a dataframe
# for (key, value) in student_dataframe.items():
#     print(value)

# loop through rows of a data frame
for (index, row) in student_dataframe.iterrows():
    print(row.student)

# {new_key:new_value for (index, row) in df.iterrows()}