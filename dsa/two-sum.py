elems = [1,2,3,4,5]
target = 8


# Normal Approach (No Caching):
def two_sum():
    for x in range(len(elems)):
        for y in range(x + 1, len(elems)):
            if elems[x] + elems[y] == target:
                return [x, y]
            
    return None

print(two_sum())



def two_sum_dict():
    hasher = {}
    
    for idx, item in enumerate(elems):
        complement =  target - item
        
        if complement in hasher:
            return [hasher[complement], idx]
        
        hasher[item] = idx
        
    return None

print(two_sum_dict())