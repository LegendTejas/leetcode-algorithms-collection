"""
LeetCode 3: Longest Substring Without Repeating Characters
Difficulty: Medium

Concept:
---------
This is a **variable-size sliding window** problem.

- We need the longest substring with no duplicate characters.
- Use two pointers (left, right) to define a window.
- Expand right pointer to include characters.
- If a character repeats, shrink the window from the left until duplicates are removed.
- Track the maximum length during the process.

Time Complexity: O(n)
Space Complexity: O(n) for the set/dictionary
"""

def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # If duplicate, shrink from left until valid
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character and update max length
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len


# Example Run
if __name__ == "__main__":
    s = "abcabcbb"
    print("Input:", s)
    print("Longest substring without repeating characters:", lengthOfLongestSubstring(s))
