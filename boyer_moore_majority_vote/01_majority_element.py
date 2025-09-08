"""
LeetCode 169 - Majority Element
--------------------------------
Problem:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n/2⌋ times.

Approach:
Boyer-Moore Majority Vote Algorithm:
1. Pick a candidate using vote cancellation.
2. Verify if the candidate is indeed the majority.

Time: O(n)
Space: O(1)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
        
            count += 1 if candidate == num else -1

        return candidate
