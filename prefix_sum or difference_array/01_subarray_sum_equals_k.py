"""
LeetCode 560: Subarray Sum Equals K
Difficulty: Medium

Concept:
---------
- This problem is a classic **Prefix Sum with HashMap** use case.
- Idea: The sum of a subarray (i..j) can be represented as:
      prefix[j] - prefix[i-1] = k
- Rearranging:
      prefix[i-1] = prefix[j] - k
- So, while computing prefix sum, we check how many times
  (current_sum - k) appeared before.
- This avoids nested loops (O(n^2)) and achieves O(n).

Time Complexity: O(n)
Space Complexity: O(n)
"""

def subarraySum(nums: List[int], k: int) -> int:
    prefix_count = defaultdict(int)
    prefix_count[0] = 1  # Base case: sum starts at 0
    
    curr_sum = 0
    result = 0
    
    for num in nums:
        curr_sum += num
        # If (curr_sum - k) has appeared before, those subarrays add to k
        result += prefix_count[curr_sum - k]
        prefix_count[curr_sum] += 1
    
    return result


# Example Run
if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 3
    print("Input:", nums, "Target Sum:", k)
    print("Number of Subarrays with sum =", k, ":", subarraySum(nums, k))
