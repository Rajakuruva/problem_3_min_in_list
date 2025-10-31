#  Problem 3: Find Minimum Element in a List

---

##  Problem Statement
Write a Python program to find the **minimum element** in a list of integers.  
First, implement it **manually using loops**, and then using Python’s built-in `min()` function.

---

##  Example
| Input | Output |
|--------|--------|
| `[4, 7, 2, 9, 5]` | `2` |
| `[-3, -8, -2]` | `-8` |
| `[12, 12, 12, 12]` | `12` |
| `[]` | `"Please provide a valid array"` |
| `[123]` | `123` |

---

##  Approach 1 — Manual Iteration

1. Check if the list is empty — if yes, return `"Please provide a valid array"`.  
2. Initialize the first element as the smallest (`min_value = array[0]`).  
3. Traverse the list starting from index `1`.  
4. If any element is smaller than `min_value`, update it.  
5. Return `min_value` after completing traversal.

---

##  Time & Space Complexity
- **Time Complexity:** O(n) — single pass through the list  
- **Space Complexity:** O(1) — only one variable (`min_value`) is used

---

##  Code
```python
# Method1: Using Simple Loop
def find_min_value(array):
    len_array = len(array)                         # O(1)
    if len_array == 0:
        return "Please provide a valid array"
    
    min_value = array[0]                           # O(1)
    for value in range(1, len_array):              # O(n)
        if array[value] < min_value:
            min_value = array[value]
    return min_value


# Test Cases
data_1 = [31, 23, 546, 23, 1]         # Positive values
data_2 = []                           # Empty list
data_3 = [-1, -23, 0, 3213, 2, 12]    # Negative and positive values
data_4 = [1, 1, 1, 1]                 # All same values
data_5 = [123]                        # Single value

print("Case1: Min value :", find_min_value(data_1))
print("Case2: Min value :", find_min_value(data_2))
print("Case3: Min value :", find_min_value(data_3))
print("Case4: Min value :", find_min_value(data_4))
print("Case5: Min value :", find_min_value(data_5))
```

---
##  Approach 2 — Using Built-in Function min()

1. Check if the list is empty — if yes, return "Please provide a valid array".
2. Use Python’s built-in min() function to get the smallest element.
---

##  Time & Space Complexity
- **Time Complexity:** O(n) — single pass through the list  
- **Space Complexity:** O(1)

---
```python
# Method2: Using Built-in Method
def find_min_value_using_built_in_method(array_data):
    if len(array_data) == 0:
        return "Please provide a valid array"
    return min(array_data)  # O(n)


# Test Cases
user_data_1 = [31, 23, 546, 23, 1]
user_data_2 = []
user_data_3 = [-1, -23, 0, 3213, 2, 12]
user_data_4 = [1, 1, 1, 1]
user_data_5 = [123]

print("Case1: Min value :", find_min_value_using_built_in_method(user_data_1))
print("Case2: Min value :", find_min_value_using_built_in_method(user_data_2))
print("Case3: Min value :", find_min_value_using_built_in_method(user_data_3))
print("Case4: Min value :", find_min_value_using_built_in_method(user_data_4))
print("Case5: Min value :", find_min_value_using_built_in_method(user_data_5))
```
---

## Sample Output
```
Case1: Min value : 1
Case2: Min value : Please provide a valid array
Case3: Min value : -23
Case4: Min value : 1
Case5: Min value : 123
``
