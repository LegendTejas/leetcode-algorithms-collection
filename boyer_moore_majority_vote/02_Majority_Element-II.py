"""
LeetCode 229 - Majority Element II
-----------------------------------
Problem:
Find all elements in the array that appear more than ⌊n/3⌋ times.

Approach:
Extended Boyer-Moore Algorithm:
1. There can be at most 2 majority elements (> n/3).
2. Use two counters to find two candidates.
3. Verify counts in a second pass.

Time: O(n)
Space: O(1)
"""

def majorityElementII(nums):
    if not nums:
        return []

    # Phase 1: Find candidates
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0

    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1, count2 = count1 - 1, count2 - 1

    # Phase 2: Verify
    result = []
    for c in [candidate1, candidate2]:
        if nums.count(c) > len(nums) // 3:
            result.append(c)

    return result

# Example
print("Majority Elements (> n/3):", majorityElementII([3,2,3]))   # Output: [3]
print("Majority Elements (> n/3):", majorityElementII([1,1,1,3,3,2,2,2]))  # Output: [1,2]
