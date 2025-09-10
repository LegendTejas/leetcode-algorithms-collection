"""
LeetCode 53: Maximum Subarray
Difficulty: Medium

Concept:
---------
This uses **Kadane's Algorithm**.

- At each index, either extend the current subarray or start a new one.
- Keep track of the maximum sum.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_max = nums[0]
        current_sum = 0
        for i in nums:
            current_sum += i
            sum_max = max(current_sum,sum_max)
            if current_sum < 0:
                current_sum = 0
        return sum_max
