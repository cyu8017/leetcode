from typing import List

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        jumbo = tomatoSlices // 2 - cheeseSlices
        small = cheeseSlices - jumbo
        return [jumbo, small] if tomatoSlices % 2 == 0 and jumbo >= 0 and small >= 0 else []
