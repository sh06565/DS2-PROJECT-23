import pandas as pd
import time 
# define the exponential search function
def exponential_search(arr, x):
    if arr[0] == x:
        return 0, 0
    elif arr[-1] == x:
        return len(arr) - 1, len(arr) - 1
    else:
        i = 1
        while i < len(arr) and arr[i] <= x:
            i *= 2
        left = i // 2
        right = min(i, len(arr) - 1)
        return binary_search(arr, left, right, x)

# define the binary search function
def binary_search(arr, left, right, x):
    if right >= left:
        mid = (left + right) // 2
        print(arr[mid],x)

        if arr[mid] == x:
            # find the range of rows with the matching value
            start, end = mid, mid
            while start > left and arr[start - 1] == x:
                start -= 1
            while end < right and arr[end + 1] == x:
                end += 1
            return start, end
        elif arr[mid] > x:
            return binary_search(arr, left, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, right, x)
    else:
        return -1, -1

# read the first 1 rows of the dataset
attr = pd.read_csv('companies_sorted.csv', nrows=1)

# read the data set 
df = pd.read_csv('companies_sorted.csv', nrows=700000)

# get all the column names/attributes except the first column
attributes = attr.columns.tolist()[1:]

# print the attributes
print("List of attributes:")
for i, attribute in enumerate(attributes):
    print(f"{i+1}. {attribute}")

# prompt the user to select an attribute
selected_attribute_index = int(input("Enter the index of the attribute you want to select: "))
selected_attribute = attributes[selected_attribute_index - 1]

# print the selected attribute
print(f"You have selected '{selected_attribute}' as the attribute to search.")

# sort the dataset based on the selected attribute
df = df.sort_values(by=[selected_attribute])
print(df)

# prompt the user to enter the search value
search_value = input(f"Enter the value to search in '{selected_attribute}': ")

# record start time
start_time = time.perf_counter()

# perform exponential search to find the row indices with the matching value
left, right = exponential_search(df[selected_attribute].values, search_value)

# record end time
end_time = time.perf_counter()

print(left,right)
# # retrieve the rows with the matching value in the selected attribute column
# matching_rows = df.iloc[left:right+1]

if left == -1 and right == -1:
    print("Search value does not exist")
else:
    matching_rows = df.iloc[left:right+1]
    matching_rows = matching_rows[matching_rows[selected_attribute] == search_value]
    if len(matching_rows) == 0:
        print("Search value does not exist")
    else:
        print("Matching rows:")
        print(matching_rows)

# if left == -1 and right == -1:
#     print("Search value does not exist")
# else:
#     result=[]
#     # iterate over the rows in the returned range and check if each row has the desired value
#     for i in range(left, right+1):
#         if df[selected_attribute][i] == search_value:
#             result.append(df.iloc[i])
#     print # the matching rows
#     print(result) #for simple format 
#     print("Matching rows:")
#     print(pd.concat(result, axis=1).T)
    

print()

# calculate the execution time in milliseconds
execution_time = (end_time - start_time) * 1000

# print execution time
print(f"Execution time: {execution_time:.2f} milliseconds")
