from typing import List

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        masks = [0] * 31
        for x in range(2, 31):
            m = 0
            y = x
            ok = True
            for i, p in enumerate(primes):
                if y % p == 0:
                    if (y // p) % p == 0:
                        ok = False
                        break
                    m |= 1 << i
                    y //= p
            masks[x] = -1 if not ok else m

        cnt = [0] * 31
        for v in nums:
            cnt[v] += 1

        dp = [0] * (1 << len(primes))
        dp[0] = 1
        for x in range(2, 31):
            if cnt[x] == 0 or masks[x] < 0:
                continue
            m = masks[x]
            for state in range((1 << len(primes)) - 1, -1, -1):
                if state & m:
                    continue
                dp[state | m] = (dp[state | m] + dp[state] * cnt[x]) % MOD

        ans = sum(dp[1:]) % MOD
        # multiply by 2^cnt[1] for optional ones
        ans = ans * pow(2, cnt[1], MOD) % MOD
        return ans
