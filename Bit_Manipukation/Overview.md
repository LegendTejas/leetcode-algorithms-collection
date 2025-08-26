# Bit Manipulation Overview

Bit Manipulation is a set of techniques that use **binary representations** of numbers 
to solve problems efficiently. Common tricks involve **XOR, AND, OR, shifts, and bitmasking**.

---

## 🔹 Common Tricks
1. **XOR Properties**
   - `x ^ x = 0`
   - `x ^ 0 = x`
   - Used for finding unique elements, swapping without temp, etc.

2. **Check if ith bit is set**

if (num >> i) & 1 == 1:
bit is set


3. **Set/Unset ith bit**

num | (1 << i) # set
num & ~(1 << i) # unset


4. **Count Set Bits**
- Brian Kernighan’s Trick:
  ```
  while n > 0:
      n = n & (n - 1)   # removes the rightmost set bit
      count += 1
  ```

---

## Pseudocode: XOR Trick (Single Number)
```
function singleNumber(nums):
result = 0
for num in nums:
result = result XOR num
return result
```


---

## Pseudocode: Counting Bits
```
function countBits(n):
dp[0] = 0
for i from 1 to n:
dp[i] = dp[i >> 1] + (i & 1)
return dp
```


---

## Pseudocode: Maximum XOR (Bitmasking)
```
function findMaximumXOR(nums):
max_xor = 0
mask = 0

for bit from 31 down to 0:
    mask = mask OR (1 << bit)
    prefixes = set(num AND mask for num in nums)
    
    candidate = max_xor OR (1 << bit)
    if there exists prefix such that (candidate XOR prefix) in prefixes:
        max_xor = candidate

return max_xor
```


---

## Example Problems

- **Single Number** (LeetCode 136)
- **Counting Bits** (LeetCode 338)
- **Maximum XOR of Two Numbers** (LeetCode 421)
- **Single Number II** (LeetCode 137)
