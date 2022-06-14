class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"User first name: {self.first_name}")
        print(f"User last name: {self.last_name}")
        print(f"User email: {self.email}")
        print(f"User age: {self.age}")
        print(f"Reward member: {self.is_rewards_member}")
        print(f"Gold card points: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200

    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("Your points are not enough")


# create new instance
user1 = User("Adam", "Smith", "adam.smith@gmail.com", "52")
user2 = User("Maria", "Anderson", "manderson@yahoo.com", "32")
user3 = User("Kevin", "Harris", "kevin.harris@hotmail.com", "21")


# check display_info()
user1.display_info()


# check enroll()
user2.enroll()
user2.display_info()    # Reward memebr becomes True, and Gold card points become 200
user2.enroll()   # check enroll() again -  output: User already a member


# check spend_points()
user1.spend_points(50)     # output: Your points are not enough
user2.spend_points(80)

user1.display_info()
user2.display_info()    # Gold card points reduces to 120
user3.display_info()
