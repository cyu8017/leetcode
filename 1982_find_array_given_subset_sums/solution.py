from collections import Counter
from typing import List

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums = sorted(sums)
        ans: List[int] = []
        for _ in range(n):
            d = sums[1] - sums[0]
            count = Counter(sums)
            without: List[int] = []
            with_d: List[int] = []
            for x in sums:
                if count[x] == 0:
                    continue
                count[x] -= 1
                count[x + d] -= 1
                without.append(x)
                with_d.append(x + d)
            # Decide whether d or -d belongs to the array
            if 0 in without:
                ans.append(d)
                sums = without
            else:
                ans.append(-d)
                sums = with_d
        return ans
