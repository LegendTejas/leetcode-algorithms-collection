"""
LeetCode 11: Container With Most Water
Difficulty: Medium

Concept:
---------
This is one of the most famous **Two Pointers problems**.

- You are given an array where each index represents a vertical line at that height.
- You need to find the maximum water that can be trapped between two lines.
- Brute force would compare all pairs (O(n^2)), but we can do it in O(n) using two pointers:
  - Start with the widest container (left at 0, right at n-1).
  - Calculate the area: min(height[left], height[right]) * (right - left).
  - Move the pointer pointing to the smaller height inward because:
    - The area is limited by the shorter line.
    - Moving the taller line won’t help (since width decreases), but moving the smaller might give a taller line.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        # Width between the two lines
        width = right - left
        # Height is limited by the shorter line
        curr_height = min(height[left], height[right])
        # Calculate area
        curr_area = width * curr_height
        max_water = max(max_water, curr_area)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water


# Example Run
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print("Heights:", height)
    print("Maximum water area:", max_area(height))
