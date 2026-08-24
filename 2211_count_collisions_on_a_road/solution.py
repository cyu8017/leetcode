# LeetCode 2211 - Count Collisions on a Road
# https://leetcode.com/problems/count-collisions-on-a-road/
class Solution:
    def countCollisions(self, directions: str) -> int:
        i = 0
        j = len(directions) - 1
        while i < len(directions) and directions[i] == "L":
            i += 1
        while j >= 0 and directions[j] == "R":
            j -= 1
        ans = 0
        for k in range(i, (j) + 1):
            if directions[k] != "S":
                ans += 1
        return ans
