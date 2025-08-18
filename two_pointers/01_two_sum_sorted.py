"""
LeetCode 167: Two Sum II - Input Array Is Sorted
Difficulty: Medium

Concept:
---------
This problem is a classic example of the **Two Pointers technique**.

- Given a sorted array, we need to find two numbers such that they add up to a target.
- Instead of using brute force (O(n^2)), we can use two pointers:
  - One pointer starts from the left (smallest value).
  - Another pointer starts from the right (largest value).
- If their sum is too large → move the right pointer leftward.
- If their sum is too small → move the left pointer rightward.
- If equal → we found the answer.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        
        if curr_sum == target:
            # +1 for 1-based indexing as required by LeetCode
            return [left + 1, right + 1]
        
        elif curr_sum < target:
            left += 1  # Need a larger sum → move left pointer right
        
        else:
            right -= 1  # Need a smaller sum → move right pointer left
    
    return []  # If no solution is found (though guaranteed one exists in LeetCode)
    

# Example Run
if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print("Input:", numbers, "Target:", target)
    print("Output (1-based indices):", two_sum_sorted(numbers, target))
