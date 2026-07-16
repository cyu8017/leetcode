# LeetCode 0914 - X of a Kind in a Deck of Cards
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

from collections import Counter
from math import gcd
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        counts = list(Counter(deck).values())
        g = reduce(gcd, counts)
        return g >= 2
