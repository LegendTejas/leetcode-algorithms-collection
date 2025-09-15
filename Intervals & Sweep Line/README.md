# Intervals & Sweep Line

## Concept
Intervals and the Sweep Line algorithm are powerful techniques to solve scheduling, merging, and resource allocation problems.  

### Intervals
- An interval is represented as `[start, end]`.
- Common tasks:
  - Detecting overlaps
  - Merging intervals
  - Inserting new intervals
  - Finding the maximum number of active intervals

### Sweep Line
The **Sweep Line** technique converts interval problems into **events**:
- Represent **start** of interval as `+1`.
- Represent **end** of interval as `-1`.
- Sort events by position, then **sweep** from left to right while keeping track of active intervals/resources.

---

## Intuition
1. **Intervals**
   - Sort by start or end.
   - Use greedy strategies or merging rules to decide overlaps.
   - Efficient for overlap detection and merging.

2. **Sweep Line**
   - Think of a vertical line sweeping across a timeline.
   - Track how many intervals are active at any point.
   - Useful in meeting rooms, car pooling, skyline problems.

---

## Steps for Sweep Line
1. Convert each interval `[start, end]` into two events:
   - `(start, +1)`
   - `(end, -1)`
2. Sort events by position (and handle ties carefully).
3. Traverse events in order:
   - Add `+1` when encountering a start.
   - Subtract `-1` when encountering an end.
   - Keep track of the maximum active count if needed.

---

## Pseudocode

### Generic Sweep Line

```
function sweepLine(intervals):
events = []
for (start, end) in intervals:
events.append((start, +1))
events.append((end, -1))
sort(events)   # sort by position, handle ties carefully

active = 0
max_active = 0
for (pos, change) in events:
    active += change
    max_active = max(max_active, active)

return max_active
```

---

### Time and Space Complexity
- **Time Complexity**:  
  - Sorting intervals/events → `O(n log n)`  
  - Traversal/greedy merge → `O(n)`  
  - Overall: `O(n log n)`

- **Space Complexity**:  
  - `O(n)` for events or merged intervals.

---

## LeetCode Problems with Intervals & Sweep Line

1. **LeetCode 56 - Merge Intervals**  
   Merge overlapping intervals.

2. **LeetCode 57 - Insert Interval**  
   Insert a new interval and merge overlaps.

3. **LeetCode 252 - Meeting Rooms**  
   Check if a person can attend all meetings (interval overlap check).

4. **LeetCode 253 - Meeting Rooms II**  
   Find minimum number of meeting rooms (sweep line with heap).

5. **LeetCode 435 - Non-overlapping Intervals**  
   Remove the minimum number of intervals to avoid overlaps.

6. **LeetCode 1094 - Car Pooling**  
   Use sweep line to check if passengers exceed car capacity.

---
