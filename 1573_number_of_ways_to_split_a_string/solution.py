from typing import List

class Solution:
    def numWays(self, s: str) -> int:
        MOD = 1_000_000_007
        ones = s.count("1")
        if ones % 3:
            return 0
        if ones == 0:
            gaps = len(s) - 1
            return gaps * (gaps - 1) // 2 % MOD
        target = ones // 3
        positions = [i for i, ch in enumerate(s) if ch == "1"]
        return (positions[target] - positions[target - 1]) * (positions[2 * target] - positions[2 * target - 1]) % MOD
