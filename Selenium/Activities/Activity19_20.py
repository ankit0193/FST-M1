import pandas as pd
from pandas import ExcelWriter

#Activity19

data = {
	'FirstName':["Satvik", "Avinash", "Lahri"],
	'LastName':["Shah", "Kati", "Rath"],
	'Email':["satshah@example.com", "avinashK@example.com", "lahri.rath@example.com"],
	'PhoneNumber':["4537829158", "4892184058", "4528727830"]
}

df = pd.DataFrame(data)

writer = ExcelWriter("./sample.xlsx")
df.to_excel(writer, sheet_name='Sheet1', index = False)

writer.close()

# Activity20
dataframe = pd.read_excel('./sample.xlsx')

print(dataframe)

print("====================================")
print("Number of rows and columns:", dataframe.shape)

print("====================================")
print("Emails:")
print(dataframe['Email'])

print("====================================")
print("Sorted data:")
print(dataframe.sort_values('FirstName'))