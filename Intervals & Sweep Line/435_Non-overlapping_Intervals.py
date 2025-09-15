"""
LeetCode 435. Non-overlapping Intervals
---------------------------------------
Find the minimum number of intervals to remove to make the rest non-overlapping.

Approach:
- Sort intervals by end time
- Greedily keep intervals with earliest end
- Count overlaps that must be removed
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])  # sort by end
        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                count += 1  # overlap, remove this
            else:
                prev_end = intervals[i][1]
        
        return count
