# empty list
from typing import List


my_list = []

# str fruit list
super_list = ["apple", "mango", "banana", "orange", "kiwi", "pomegranate"]


# Iteration:
for eachItem in super_list:
    print(f"Item Name: {eachItem}")
    

# Let's update the list
new_fruits = ["strawberries", "grapes", "avocado", "pineapple", "watermelon"]

super_list.extend(new_fruits);
super_list.append("Fig")
super_list.insert(-1, "SnakeDragon")
print("Value Index", super_list.index("Fig"))


capitalized_list = [x.capitalize() for x in super_list]

print(capitalized_list)


# Let's do list comprehension:
print(super_list[0:], flush=True)
super_list[:5]
super_list[:4+1]
print(super_list[0::])





# Advanced Python:
nums = [1, 2, 3, 4, 5]
nums = [item ** item for item in nums]
print(nums)


# New (conditional)
conditional_list = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(conditional_list)


# Unpacking List
nums  = [1, 2, 3, 4, 5, 6]
a, b, c = nums[:3]
d, e, f = nums[3:]

print(a, b, c, end="\n")
print(d, e, f)


# Nested (CheatGPT copied just for learning purpose):
def max_depth(lst):
    # Base case: if it's not a list or it's an empty list
    if not isinstance(lst, list) or not lst:
        return 0
    else:
        # Recursively find the max depth of sublists
        return 1 + max(max_depth(item) for item in lst)

def flatten(lst):
    # Check if the current element is a list or not
    flat = []
    for item in lst:
        if isinstance(item, list):
            # If it's a list, go deeper
            flat.extend(flatten(item))
        else:
            # If it's not a list, just append the item
            flat.append(item)
    return flat

# Example list with varying levels of nesting
nested = [[1, 2], [3, 4], [5, 6], [[1, 3, 5]]]

# Step 1: Find the max depth
depth = max_depth(nested)
print(f"Maximum Depth: {depth}")

# Step 2: Flatten the list to the maximum depth
flat_list = flatten(nested)
print(f"Flattened List: {flat_list}")
