class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # can set default value


# Creating user
user_1 = User("001", "Aryadeep")

user_2 = User("002", "Sanchita")

print(user_1.username)
print(user_2.username)

print(user_1.followers)
