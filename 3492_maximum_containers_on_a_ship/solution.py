# LeetCode 3492 - Maximum Containers on a Ship
# https://leetcode.com/problems/maximum-containers-on-a-ship/


class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        cap = n * n
        by_w = maxWeight // w
        return cap if cap < by_w else by_w
