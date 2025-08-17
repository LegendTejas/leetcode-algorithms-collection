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
