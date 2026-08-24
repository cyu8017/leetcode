# LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

from typing import List


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def gcdll(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        def lcmll(a: int, b: int) -> int:
            return a // gcdll(a, b) * b

        def bit_count(x: int) -> int:
            c = 0
            while x != 0:
                c += x & 1
                x >>= 1
            return c

        n = len(coins)

        def check(mx: int) -> bool:
            cnt = 0
            for i in range(1, 1 << n):
                v = 1
                for j in range(n):
                    if ((i >> j) & 1) != 0:
                        v = lcmll(v, coins[j])
                        if v > mx:
                            break
                m = bit_count(i)
                if m % 2 == 1:
                    cnt += mx // v
                else:
                    cnt -= mx // v
            return cnt >= k

        lo, hi = 1, 100000000000
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
