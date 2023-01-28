class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # can set default value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# Creating user
user_1 = User("001", "Aryadeep")

user_2 = User("002", "Sanchita")

print(user_1.username)
print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
