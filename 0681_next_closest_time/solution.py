# LeetCode 0681 - Next Closest Time
# https://leetcode.com/problems/next-closest-time/


class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = set(time[:2] + time[3:])
        start = int(time[:2]) * 60 + int(time[3:])
        for delta in range(1, 24 * 60 + 1):
            mins = (start + delta) % (24 * 60)
            hh, mm = divmod(mins, 60)
            candidate = f"{hh:02d}{mm:02d}"
            if set(candidate) <= digits:
                return f"{hh:02d}:{mm:02d}"
        return time
