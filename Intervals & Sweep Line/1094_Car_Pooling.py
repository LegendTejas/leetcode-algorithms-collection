"""
LeetCode 1094. Car Pooling
--------------------------
You are driving a vehicle with a given capacity. 
Trips[i] = [num_passengers, start, end].
Return True if capacity is never exceeded.

Approach:
- Use sweep line technique
- Treat start as +passengers, end as -passengers
"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for passengers, start, end in trips:
            events.append((start, passengers))
            events.append((end, -passengers))

        events.sort()
        curr_passengers = 0

        for _, change in events:
            curr_passengers += change
            if curr_passengers > capacity:
                return False
        return True
