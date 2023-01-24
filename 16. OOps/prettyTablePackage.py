# package prettytable imported Prettytable class
from prettytable import PrettyTable

# create object from the PrettyTable Class
table = PrettyTable()  # constructed new object table
# add_column is method
table.add_column("col1", ["abra", "ka", "dabra", "gili", "gili", "chuu"])
table.add_column("col2", ["abba", "ka", "bharosa", "jitna", "padega", "ree"])
# align is an attribute
table.align = "l"  # align to left hand margin
print(table)
