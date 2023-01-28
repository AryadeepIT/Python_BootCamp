class Dog:
    def __init__(self):  # constructor formation
        # self -> actual object being created
        print("New Dog being Created...")
        # init function will call everytime when object create from this class


dog_1 = Dog()  # new dog being created
dog_1.id = "BHUK001"
dog_1.dogname = "Lalu Bhuk Bhuk"

print(dog_1.dogname)

dog_2 = Dog()   # new dog being created
dog_2.id = "BHUK002"
dog_2.dogname = "Sadhu Bhuk Bhuk"