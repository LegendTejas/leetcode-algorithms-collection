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

def majorityElement(nums):
    # Phase 1: Find candidate
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Phase 2: Verify (optional for LeetCode 169, since majority always exists)
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return -1

# Example
print("Majority Element:", majorityElement([3,2,3]))   # Output: 3
print("Majority Element:", majorityElement([2,2,1,1,1,2,2]))  # Output: 2
