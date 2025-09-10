## Sliding Window Technique

The Sliding Window technique is used to reduce nested loops into a single loop by maintaining a window (subarray/substring) that slides across the input.
It is very effective for problems involving subarrays/substrings, especially when we need to maintain some condition (like sum, length, frequency, etc.).

---

## Generic Sliding Window Pseudocode
```
function slidingWindow(array, k):
    left ← 0
    right ← 0
    window_sum ← 0
    result ← -∞   # or some initial value depending on problem

    while right < length(array):
        # Expand the window by including array[right]
        window_sum ← window_sum + array[right]

        # If window size exceeds k, shrink it from the left
        if (right - left + 1) > k:
            window_sum ← window_sum - array[left]
            left ← left + 1

        # Update result when window size is valid
        if (right - left + 1) == k:
            result ← max(result, window_sum)

        right ← right + 1

    return result

```
---

### Example Problem: Maximum Sum Subarray of Size K

**Problem:** Given an array of integers, find the maximum sum of any subarray of size `k`.

**Pseudocode**:
```
function maxSumSubarray(array, k):
    left ← 0
    window_sum ← 0
    max_sum ← -∞

    for right from 0 to length(array)-1:
        window_sum ← window_sum + array[right]

        if (right - left + 1) == k:
            max_sum ← max(max_sum, window_sum)
            window_sum ← window_sum - array[left]
            left ← left + 1

    return max_sum

```
