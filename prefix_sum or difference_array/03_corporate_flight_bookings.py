"""
LeetCode 1109: Corporate Flight Bookings
Difficulty: Medium

Concept:
---------
- This is a **Difference Array problem** (reverse of prefix sum).
- Instead of updating each index in range [l, r], we:
    - Add `seats` at index l
    - Subtract `seats` at index r+1
- After processing all bookings, take prefix sum of diff array
  to get final seat bookings per flight.

Time Complexity: O(n + m) where m = number of bookings
Space Complexity: O(n)
"""

def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    diff = [0] * (n + 1)
    
    # Apply difference array updates
    for l, r, seats in bookings:
        diff[l-1] += seats
        if r < n:
            diff[r] -= seats
    
    # Convert difference array → prefix sum
    res = [0] * n
    res[0] = diff[0]
    for i in range(1, n):
        res[i] = res[i-1] + diff[i]
    
    return res


# Example Run
if __name__ == "__main__":
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    print("Bookings:", bookings, "Flights:", n)
    print("Final seat bookings per flight:", corpFlightBookings(bookings, n))
