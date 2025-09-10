"""
LeetCode 643: Maximum Average Subarray I
Difficulty: Easy

Concept:
---------
This is a classic **fixed-size sliding window** problem.

- We need to find the maximum average of any contiguous subarray of size k.
- Instead of recalculating the sum each time (O(n*k)), we:
  - Keep a running sum of the current window.
  - Slide the window by subtracting the element going out (left) 
    and adding the element coming in (right).
- This reduces complexity to O(n).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = max_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            
            # Subtract the left element of the window
            # Add the right element of the window
            window_sum += nums[i] - nums[i - k]
            
            #update the max_sum
            max_sum = max(max_sum, window_sum)
        
        # return the maximum average
        return max_sum / k
