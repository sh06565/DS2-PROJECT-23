import pandas as pd

# read the dataset
df = pd.read_csv('companies_sorted.csv', nrows=0)

# get all the column names/attributes
attributes = df.columns.tolist()[1:]

# print the attributes
print("List of attributes:")
for i, attribute in enumerate(attributes):
    print(f"{i+1}. {attribute}")

# prompt the user to select an attribute
selected_attribute_index = int(input("Enter the index of the attribute you want to select: "))
selected_attribute = attributes[selected_attribute_index - 1]

# print the selected attribute
print(f"You have selected '{selected_attribute}' as the attribute to search.")
