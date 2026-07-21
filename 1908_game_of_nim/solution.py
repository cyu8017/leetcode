from functools import reduce
from operator import xor
from typing import List

class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        return reduce(xor, piles, 0) != 0
