"""
LeetCode 137: Single Number II
Difficulty: Hard

Problem:
--------
Given an integer array `nums` where every element appears exactly three times 
except for one element, which appears exactly once. Find the single element 
that appears once.

You must implement a solution with linear runtime complexity (O(n)) and 
use only constant extra space (O(1)).

Concept:
--------
Key Idea: Bit Manipulation (Bitmasking)

- Every number except one appears 3 times.
- If we count the number of set bits at each bit position:
    - Those counts should be multiples of 3 (for elements appearing 3 times).
    - The leftover (not divisible by 3) belongs to the single unique number.

Approach 1 (Bit Counting):
--------------------------
- For each bit position (0 to 31), count how many numbers have that bit set.
- Take modulo 3 of this count → gives whether the unique number has that bit set.
- Construct the answer bit by bit.

Approach 2 (Optimized Bitmasking Trick):
----------------------------------------
We use two variables (bitmasks) to represent bits seen once and twice:
    ones   → bits seen exactly once
    twos   → bits seen exactly twice

Algorithm:
1. For each number in nums:
      - Update "ones" as XOR with num, but remove any bits that are already in "twos".
      - Update "twos" as XOR with num, but remove any bits that are already in "ones".
2. At the end, "ones" will contain the unique number.

Time Complexity: O(n)
Space Complexity: O(1)

Let's implement both for clarity.
"""

from typing import List

# -------------------------------
# Approach 1: Bit Counting Method
# -------------------------------
def singleNumber_bitCount(nums: List[int]) -> int:
    result = 0
    for i in range(32):  # assume 32-bit integers
        bit_sum = 0
        for num in nums:
            if (num >> i) & 1:  # check if ith bit is set
                bit_sum += 1
        if bit_sum % 3:  # leftover bit belongs to unique number
            # Handle negative numbers (sign bit at position 31)
            if i == 31:
                result -= (1 << 31)
            else:
                result |= (1 << i)
    return result


# -----------------------------------
# Approach 2: Optimized Bitmasking DP
# -----------------------------------
def singleNumber_bitmask(nums: List[int]) -> int:
    ones, twos = 0, 0
    for num in nums:
        # Update ones (store bits seen once)
        ones = (ones ^ num) & ~twos
        # Update twos (store bits seen twice)
        twos = (twos ^ num) & ~ones
    return ones  # unique number stored in ones


# Example Run
if __name__ == "__main__":
    nums = [2, 2, 3, 2]
    print("Input:", nums)
    print("Unique Number (Bit Count Method):", singleNumber_bitCount(nums))
    print("Unique Number (Bitmask Method):", singleNumber_bitmask(nums))

    nums2 = [0,1,0,1,0,1,99]
    print("\nInput:", nums2)
    print("Unique Number (Bit Count Method):", singleNumber_bitCount(nums2))
    print("Unique Number (Bitmask Method):", singleNumber_bitmask(nums2))
