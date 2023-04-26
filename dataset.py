import csv

# open the file in read mode
with open('companies_sorted.csv', newline='') as csvfile:
    # create a CSV reader object
    reader = csv.reader(csvfile)

    # read the first row of the file, which should contain the column names
    column_names = next(reader)

# print the column names
print("List of attributes:")
for attribute in column_names:
    print(attribute)
