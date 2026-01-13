class chai:
    size="small"

    def describe(self):
        return f"This is a {self.size} chai."

cup=chai()
# print(chai.size())
# print(chai.describe())
# print(cup.describe())
# print(chai.describe(cup))


cup_two=chai()
cup_two.size="large"
print(chai.describe(cup_two))
print(chai.describe(cup_two.size))
