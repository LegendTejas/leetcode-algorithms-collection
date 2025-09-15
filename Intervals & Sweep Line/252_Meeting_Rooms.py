"""
LeetCode 252. Meeting Rooms
---------------------------
Given meeting time intervals, determine if a person can attend all meetings.

Approach:
- Sort intervals by start time
- If any start < previous end, return False
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
