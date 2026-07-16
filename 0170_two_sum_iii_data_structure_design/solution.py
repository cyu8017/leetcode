# LeetCode 0170 - Two Sum III - Data structure design
# https://leetcode.com/problems/two-sum-iii-data-structure-design/

from collections import defaultdict


class TwoSum:
    def __init__(self):
        self.counts: dict[int, int] = defaultdict(int)

    def add(self, number: int) -> None:
        self.counts[number] += 1

    def find(self, value: int) -> bool:
        for number, count in self.counts.items():
            complement = value - number
            if complement == number:
                if count >= 2:
                    return True
            elif complement in self.counts:
                return True
        return False
