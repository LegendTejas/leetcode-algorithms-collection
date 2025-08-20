"""
LeetCode 303: Range Sum Query - Immutable
Difficulty: Easy

Concept:
---------
- Use a **Prefix Sum array** to answer range sum queries in O(1).
- Precompute prefix sums:
      prefix[i] = sum of nums[0..i-1]
- Then, range sum (l..r) = prefix[r+1] - prefix[l]

Time Complexity:
    - Precomputation: O(n)
    - Each query: O(1)
Space Complexity: O(n)
"""

class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Example Run
if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    print("Sum(0,2):", obj.sumRange(0, 2))  # Output: 1
    print("Sum(2,5):", obj.sumRange(2, 5))  # Output: -1
