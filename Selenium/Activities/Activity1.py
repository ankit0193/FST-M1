name = input("Enter your name :")
age = int(input("Enter your age :"))

year_when_100 = 2025 + (100 - age)

print(name + " will turn 100 in year" + str(year_when_100))
print(name + " will turn 100 in year {}".format(year_when_100))