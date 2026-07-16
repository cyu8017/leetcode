# LeetCode 0846 - Hand of Straights
# https://leetcode.com/problems/hand-of-straights/

from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for start in sorted(count):
            while count[start]:
                for x in range(start, start + groupSize):
                    if not count[x]:
                        return False
                    count[x] -= 1
        return True
