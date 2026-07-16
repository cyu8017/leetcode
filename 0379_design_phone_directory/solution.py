# LeetCode 0379 - Design Phone Directory
# https://leetcode.com/problems/design-phone-directory/


class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.available = set(range(maxNumbers))

    def get(self) -> int:
        if not self.available:
            return -1
        number = min(self.available)
        self.available.remove(number)
        return number

    def check(self, number: int) -> bool:
        return number in self.available

    def release(self, number: int) -> None:
        self.available.add(number)
