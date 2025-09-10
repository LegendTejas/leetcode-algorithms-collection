"""
LeetCode 1004: Max Consecutive Ones III
Difficulty: Medium

Concept:
---------
This is a **variable-size sliding window** problem.

- We need the longest subarray containing only 1's if we can flip at most k zeros.
- Use two pointers (left, right) to define the window.
- Expand right pointer to include numbers.
- Track the count of zeros in the window.
- If zeros exceed k, shrink the window from the left until valid.
- Track the maximum length during the process.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding Window - Keep track of number of zeros
        maxx = 0
        num_zeros = 0

        l = r = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1

            w = (r - l) + 1
            maxx = max(maxx, w)
    
        return maxx
