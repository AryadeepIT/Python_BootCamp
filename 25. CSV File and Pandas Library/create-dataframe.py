#  create Dataframe from Scratch
import pandas

data_dict = {
    "students": ["Aryadeep", "Sanchita", "Munu"],
    "scores": [76, 96, 99]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
