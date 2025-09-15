"""
LeetCode 253. Meeting Rooms II
------------------------------
Find the minimum number of conference rooms required.

Approach:
- Sort intervals by start time
- Use a min-heap to track end times of ongoing meetings
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        min_heap = [intervals[0][1]]  # store end times

        for start, end in intervals[1:]:
            if start >= min_heap[0]:
                heapq.heappop(min_heap)  # free a room
            heapq.heappush(min_heap, end)

        return len(min_heap)
