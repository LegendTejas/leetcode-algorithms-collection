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

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window: expand R, shrink L when duplicate found
        # W = (R - L) + 1
        L = R = longest = 0
        sett = set()

        while R < len(s):
            while s[R] in sett:  # shrink window until valid
                sett.remove(s[L])
                L += 1

            sett.add(s[R])
            W = (R - L) + 1
            longest = max(longest, W)
            R += 1  # move right pointer

        return longest
