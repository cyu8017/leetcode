# LeetCode 0278 - First Bad Version
# https://leetcode.com/problems/first-bad-version/


def isBadVersion(version: int) -> bool:
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
