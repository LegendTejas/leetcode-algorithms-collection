"""
LeetCode 152: Maximum Product Subarray
Difficulty: Medium

Concept:
---------
- Similar to Kadane’s Algorithm but with products.
- Need to track both maximum and minimum at each step (because a negative number can flip).
- At each index:
  max_current = max(num, num * max_current, num * min_current)
  min_current = min(num, num * prev_max, num * min_current)

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_curr = min_curr = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max(num, num * max_curr, num * min_curr)
            min_curr = min(num, num * max_curr, num * min_curr)
            max_curr = temp_max
            result = max(result, max_curr)

        return result
