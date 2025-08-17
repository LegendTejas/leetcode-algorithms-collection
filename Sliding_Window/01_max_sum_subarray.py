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

from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    # Initial window sum
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    
    # Return maximum average
    return max_sum / k


# Example Run
if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    print("Input:", nums, "k =", k)
    print("Maximum Average Subarray:", findMaxAverage(nums, k))
