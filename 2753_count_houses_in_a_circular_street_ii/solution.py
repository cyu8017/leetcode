# LeetCode 2753 - Count Houses in a Circular Street II
# https://leetcode.com/problems/count-houses-in-a-circular-street-ii/


class Solution:
    def houseCount(self, street, k: int) -> int:
        while not street.isDoorOpen():
            street.moveRight()
        street.closeDoor()
        street.moveRight()
        ans = 1
        for _ in range(1, k):
            if street.isDoorOpen():
                street.closeDoor()
                ans = 0
            ans += 1
            street.moveRight()
        return ans
