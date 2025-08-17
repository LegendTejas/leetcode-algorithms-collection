## Generic Two Pointers Pseudocode

```
function twoPointersAlgorithm(array):
    left ← 0
    right ← length(array) - 1
    
    while left < right:
        # Process the current pair
        doSomething(array[left], array[right])
        
        if condition_to_move_left:
            left ← left + 1
        else:
            right ← right - 1
```

### Example: Two Sum II (Sorted Array)

```
function twoSumSorted(array, target):
    left ← 0
    right ← length(array) - 1
    
    while left < right:
        sum ← array[left] + array[right]
        
        if sum == target:
            return (left+1, right+1)   # 1-based index as per problem
        
        else if sum < target:
            left ← left + 1   # Need a bigger sum
        
        else:
            right ← right - 1 # Need a smaller sum
```
