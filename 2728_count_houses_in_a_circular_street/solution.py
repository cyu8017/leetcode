# LeetCode 2728 - Count Houses in a Circular Street
# https://leetcode.com/problems/count-houses-in-a-circular-street/

from typing import List, Union


class Street:
    def __init__(self, doors: List[int]):
        self.doors = doors
        self.i = 0

    def closeDoor(self) -> None:
        self.doors[self.i] = 0

    def openDoor(self) -> None:
        self.doors[self.i] = 1

    def isDoorOpen(self) -> bool:
        return self.doors[self.i] == 1

    def moveRight(self) -> None:
        self.i = (self.i + 1) % len(self.doors)


class Solution:
    def houseCount(self, street: Union[Street, List[int]], k: int) -> int:
        if isinstance(street, list):
            street = Street(street)
        for _ in range(k):
            street.closeDoor()
            street.moveRight()
        ans = 0
        while True:
            ans += 1
            street.openDoor()
            street.moveRight()
            if street.isDoorOpen():
                break
        return ans
