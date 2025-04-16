from typing import List

def two_pointer(arr: List[int], target: int):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None  # In case no pair is found

print(two_pointer([1, 2, 3, 4, 5], 5))  # Output: [1, 4] because 2 + 5 = 7


from typing import List, Union

def super_depth(arr: List[Union[int, list]]) -> List[int]:
    normalized = []
    for item in arr:
        if isinstance(item, list):
            normalized.extend(super_depth(item))
        else:
            normalized.append(item)
    return normalized

print(super_depth([1, 2, 3, 4, [1, 2, [1, 2, 3]]]))
