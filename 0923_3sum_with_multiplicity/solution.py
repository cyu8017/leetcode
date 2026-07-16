# LeetCode 0923 - 3Sum With Multiplicity
# https://leetcode.com/problems/3sum-with-multiplicity/

from collections import Counter


class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        MOD = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count)
        ans = 0
        for i, a in enumerate(keys):
            for j in range(i, len(keys)):
                b = keys[j]
                c = target - a - b
                if c < b:
                    break
                if c not in count:
                    continue
                if a == b == c:
                    ans += count[a] * (count[a] - 1) * (count[a] - 2) // 6
                elif a == b:
                    ans += count[a] * (count[a] - 1) // 2 * count[c]
                elif b == c:
                    ans += count[a] * count[b] * (count[b] - 1) // 2
                else:
                    ans += count[a] * count[b] * count[c]
        return ans % MOD
