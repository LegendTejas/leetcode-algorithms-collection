"""
LeetCode 421: Maximum XOR of Two Numbers in an Array
Difficulty: Medium

Concept:
---------
This problem demonstrates **bitmasking with XOR**.

Approach:
1. We try to build the maximum XOR bit by bit (from MSB to LSB).
2. Use a set to store prefixes (left bits).
3. For each bit, assume current bit can be 1 and check feasibility.
4. If feasible, keep it; else discard.

Time Complexity: O(n * log(max_num))
Space Complexity: O(n)
"""

from typing import List

def findMaximumXOR(nums: List[int]) -> int:
    max_xor = 0
    mask = 0
    
    # Find MSB to LSB
    for bit in range(31, -1, -1):
        mask |= (1 << bit)
        prefixes = {num & mask for num in nums}
        
        candidate = max_xor | (1 << bit)
        if any((candidate ^ prefix) in prefixes for prefix in prefixes):
            max_xor = candidate
    
    return max_xor


# Example Run
if __name__ == "__main__":
    nums = [3,10,5,25,2,8]
    print("Input:", nums)
    print("Maximum XOR of two numbers:", findMaximumXOR(nums))
