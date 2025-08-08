import pandas as pd

#writing into csv activity17

data = {
  "Usernames": ["admin", "Charles", "Deku"],
  "Passwords": ["password", "Charl13", "AllMight"]
}

df = pd.DataFrame(data)

df.to_csv("./sample.csv" , index = False)

#reading from csv activity18

input_data = pd .read_csv("./sample.csv") 

print ("========Usernames Column=========")
print(input_data["Usernames"])

print("\n========Second Row Data========")
print(input_data["Usernames"][1],input_data["Passwords"][1])

print("\n==========Sorted Usernames Col========")
print(input_data.sort_values(by="Usernames",ascending=True))

print("\n=========Sorted Passwords Col========")
print(input_data.sort_values(by="Passwords",ascending=False))
