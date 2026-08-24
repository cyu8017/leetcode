# LeetCode 3443 - Maximum Manhattan Distance After K Changes
# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        lat = lon = 0
        for i, c in enumerate(s):
            if c == "N":
                lat += 1
            elif c == "S":
                lat -= 1
            elif c == "E":
                lon += 1
            else:
                lon -= 1
            md = abs(lat) + abs(lon)
            steps = i + 1
            cur = md + 2 * k
            if cur > steps:
                cur = steps
            if cur > ans:
                ans = cur
        return ans
