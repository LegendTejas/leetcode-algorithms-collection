"""
LeetCode 338: Counting Bits
Difficulty: Easy

Concept:
---------
We need to count number of 1-bits (set bits) for each number from 0 to n.

Trick:
- A number i can be broken into:
    i >> 1  (i divided by 2, removing last bit)
    i & 1   (checks if last bit is set)
- So:
    bits[i] = bits[i >> 1] + (i & 1)

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

def countBits(n: int) -> List[int]:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp


# Example Run
if __name__ == "__main__":
    n = 5
    print("Input:", n)
    print("Count of set bits from 0 to", n, ":", countBits(n))
