# Prefix Sum & Difference Array Overview

The **Prefix Sum** and **Difference Array** techniques are powerful tools for solving range-based problems efficiently.

---

## 🔹 Prefix Sum

**Idea:**  
Precompute cumulative sums so that any subarray sum can be answered in O(1).

### Generic Formula:
```
prefix[i] = arr[0] + arr[1] + ... + arr[i-1]
sum(l..r) = prefix[r+1] - prefix[l]
```

### Prefix Sum Pseudocode
```
function buildPrefixArray(nums):
    prefix[0] ← 0
    for i ← 1 to length(nums):
        prefix[i] ← prefix[i-1] + nums[i-1]
    return prefix

function rangeSum(prefix, left, right):
    return prefix[right+1] - prefix[left]
```

### Example Use Cases:
- Range Sum Query (LeetCode 303)
- Subarray Sum Equals K (LeetCode 560)

---

## 🔹 Difference Array

**Idea:**  
Efficiently apply updates over a range using only two operations, then compute final values using prefix sums.

### Generic Steps:
1. Initialize a difference array `diff[]`.

2. For each update (l, r, val):  
```
diff[l] += val
diff[r+1] -= val
```

3. Compute prefix sums of `diff[]` to get the final array.

### Difference Array Pseudocode
```
function applyRangeUpdates(n, updates):
    diff ← array of size n+1 initialized with 0

    for each (l, r, val) in updates:
        diff[l] ← diff[l] + val
        if r+1 < n:
            diff[r+1] ← diff[r+1] - val

    result[0] ← diff[0]
    for i ← 1 to n-1:
        result[i] ← result[i-1] + diff[i]

    return result
```

### Example Use Cases:
- Corporate Flight Bookings (LeetCode 1109)
- Range Update Problems

---

## ✅ Summary
- **Prefix Sum:** Best for answering range queries quickly.  
- **Difference Array:** Best for applying multiple range updates efficiently.  
- Together, they cover a wide variety of **array and subarray problems** in competitive programming and interviews.
