listOne = [1, 11, 22, 7, 18]
listTwo = [90, 71, 25, 88, 12]

print("First List ", listOne)
print("Second List ", listTwo)

thirdList = []

for num in listOne:
    if (num % 2 != 0):
        thirdList.append(num)

for num in listTwo:
    if (num % 2 == 0):
        thirdList.append(num)

print("result List is:")
print(thirdList)