from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    
    # Start with the first string as a base for comparison
    prefix = strs[0]

    for string in strs[1:]:
        # Reduce the prefix until it matches the beginning of the current string
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    
    return prefix

print(longestCommonPrefix(["flower", "flame", "flings"]))  # Output: "fl"
