class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window: expand R, shrink L when duplicate found
        # W = (R - L) + 1
        L = R = longest = 0
        sett = set()

        while R < len(s):
            while s[R] in sett:  # shrink window until valid
                sett.remove(s[L])
                L += 1

            sett.add(s[R])
            W = (R - L) + 1
            longest = max(longest, W)
            R += 1  # move right pointer

        return longest
