"""
LeetCode 136: Single Number
Difficulty: Easy

Concept:
---------
This is the classic XOR trick.

Properties of XOR:
    - x ^ x = 0
    - x ^ 0 = x
    - XOR is commutative and associative

So, if every element appears twice except one:
    - All duplicate pairs cancel out (x ^ x = 0).
    - The remaining number is the unique element.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

def singleNumber(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


# Example Run
if __name__ == "__main__":
    nums = [4,1,2,1,2]
    print("Input:", nums)
    print("Single Number (appears once):", singleNumber(nums))
