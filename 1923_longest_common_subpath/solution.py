from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        m = len(paths)
        BASE1, MOD1 = 911382323, 1_000_000_007
        BASE2, MOD2 = 972663749, 1_000_000_009

        def has_common(length: int) -> bool:
            if length == 0:
                return True
            common = None
            pow1 = pow(BASE1, length, MOD1)
            pow2 = pow(BASE2, length, MOD2)
            for path in paths:
                if len(path) < length:
                    return False
                h1 = h2 = 0
                seen = set()
                for i, city in enumerate(path):
                    h1 = (h1 * BASE1 + city + 1) % MOD1
                    h2 = (h2 * BASE2 + city + 1) % MOD2
                    if i >= length:
                        h1 = (h1 - (path[i - length] + 1) * pow1) % MOD1
                        h2 = (h2 - (path[i - length] + 1) * pow2) % MOD2
                    if i >= length - 1:
                        seen.add((h1, h2))
                if common is None:
                    common = seen
                else:
                    common &= seen
                if not common:
                    return False
            return True

        lo, hi = 0, min(len(p) for p in paths)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if has_common(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
