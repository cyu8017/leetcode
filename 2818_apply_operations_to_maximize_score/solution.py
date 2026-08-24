# LeetCode 2818 - Apply Operations to Maximize Score
# https://leetcode.com/problems/apply-operations-to-maximize-score/

from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 1000000007
        n = len(nums)
        max_v = max(nums) if nums else 0
        spf = [0] * (max_v + 1)
        for i in range(2, max_v + 1):
            if spf[i] == 0:
                for j in range(i, max_v + 1, i):
                    if spf[j] == 0:
                        spf[j] = i

        def prime_score(x: int) -> int:
            seen = set()
            while x > 1:
                p = spf[x]
                seen.add(p)
                while x % p == 0:
                    x //= p
            return len(seen)

        score = [prime_score(v) for v in nums]
        left = [0] * n
        right = [0] * n
        st = []
        for i in range(n):
            while st and score[st[-1]] < score[i]:
                st.pop()
            left[i] = st[-1] if st else -1
            st.append(i)
        st.clear()
        for i in range(n - 1, -1, -1):
            while st and score[st[-1]] <= score[i]:
                st.pop()
            right[i] = st[-1] if st else n
            st.append(i)
        arr = [[nums[i], (i - left[i]) * (right[i] - i)] for i in range(n)]
        arr.sort(key=lambda p: -p[0])

        def mod_pow(a: int, b: int) -> int:
            res = 1
            base = a % MOD
            exp = b
            while exp > 0:
                if exp & 1:
                    res = res * base % MOD
                base = base * base % MOD
                exp >>= 1
            return res

        ans = 1
        remain = k
        for val, cnt in arr:
            if remain <= 0:
                break
            use = cnt if cnt < remain else remain
            ans = ans * mod_pow(val, use) % MOD
            remain -= use
        return ans
