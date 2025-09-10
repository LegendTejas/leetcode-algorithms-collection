"""
LeetCode 918: Maximum Sum Circular Subarray
Difficulty: Medium

Concept:
---------
- Two cases:
  1. Subarray without wrap → Standard Kadane’s Algorithm
  2. Subarray with wrap → Total sum - minimum subarray sum
- Answer = max(case1, case2), unless all numbers are negative.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxSubarraySumCircular(self, nums):
        # Initialize values with the first element
        curr_min = curr_max = min_sum = max_sum = total_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Kadane's algorithm for max subarray
            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(max_sum, curr_max)

            # Kadane's algorithm for min subarray
            curr_min = min(nums[i], curr_min + nums[i])
            min_sum = min(min_sum, curr_min)

            # Add to total sum
            total_sum += nums[i]

        # If all elements are negative, return max_sum
        if min_sum == total_sum:
            return max_sum

        # Max of non-circular or circular subarray
        return max(max_sum, total_sum - min_sum)
