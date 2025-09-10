# Kadane's Algorithm

## Concept
Kadane's Algorithm is a **Dynamic Programming** technique used to find the maximum sum of a contiguous subarray in `O(n)` time.

### Intuition
- A subarray must be contiguous.
- At each index, we decide:
  1. Extend the current subarray by adding `arr[i]`.
  2. Start a new subarray at `arr[i]`.

### Steps
1. Initialize two variables:
   - `max_current = arr[0]`
   - `max_global = arr[0]`
2. Iterate through the array from index 1:
   - `max_current = max(arr[i], max_current + arr[i])`
   - `max_global = max(max_global, max_current)`
3. Return `max_global`.

---

## Kadane's Algorithm Pseudocode

```
function Kadane(arr):
    max_current = arr[0]
    max_global = arr[0]

    for i from 1 to length(arr) - 1:
        max_current = max(arr[i], arr[i] + max_current)
        max_global = max(max_global, max_current)

    return max_global
```

---

### Time and Space Complexity
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

---

## LeetCode Problems with Kadane's Algorithm

1. **LeetCode 53 - Maximum Subarray**  
   Find the maximum sum of a contiguous subarray.

2. **LeetCode 918 - Maximum Sum Circular Subarray**  
   Handle wrap-around case using Kadane’s Algorithm twice.

3. **LeetCode 152 - Maximum Product Subarray**  
   Variation where we track both max and min at each step.
