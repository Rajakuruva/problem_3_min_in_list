# Method1: Using simple loop
def find_min_value(array):
    len_array = len(array)                         # O(1)
    if len_array == 0:
        return "Please provide a valid array"
    
    min_value = array[0]                           # O(1)
    for value in range(1, len_array):              # O(n)
        if array[value]<min_value:
            min_value = array[value]
    return min_value

data_1 = [31, 23, 546, 23, 1]         # Positive values
data_2 = []                           # Empty list
data_3 = [-1, -23, 0, 3213, 2, 12]    # Negative and postive values
data_4 = [1 , 1, 1, 1]                # All same values
data_5 = [123]                        # Single Value

print("Case1: Min value :", find_min_value(data_1))
print("Case2: Min value :", find_min_value(data_2))
print("Case3: Min value :", find_min_value(data_3))
print("Case4: Min value :", find_min_value(data_4))
print("Case5: Min value :", find_min_value(data_5))
# Method1 Time and Space Complexity
# Time complexity: O(n)
# Memroy Complexity: O(1)

# Method2: Using Min Built-in Method
def find_min_value_builtin(array_data):
    if len(array_data) == 0:
        return "Please provide a valid array"
    return min(array_data)  # O(n)

user_data_1 = [31, 23, 546, 23, 1]         # Positive values
user_data_2 = []                           # Empty list
user_data_3 = [-1, -23, 0, 3213, 2, 12]    # Negative and postive values
user_data_4 = [1 , 1, 1, 1]                # All same values
user_data_5 = [123]                        # Single Value

print("Case1: Min value :", find_min_value_builtin(user_data_1))
print("Case2: Min value :", find_min_value_builtin(user_data_2))
print("Case3: Min value :", find_min_value_builtin(user_data_3))
print("Case4: Min value :", find_min_value_builtin(user_data_4))
print("Case5: Min value :", find_min_value_builtin(user_data_5))
# Method2 Time and Space Complexity
# Time complexity: O(n)
# Memroy Complexity: O(1)
