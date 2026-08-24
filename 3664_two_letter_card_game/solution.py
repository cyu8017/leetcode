# LeetCode 3664 - Two-Letter Card Game
# https://leetcode.com/problems/two-letter-card-game/

from typing import List


class Solution:
    def score(self, cards: List[str], x: str) -> int:
        def pair_group(arr: List[int]) -> List[int]:
            total = 0
            mx = 0
            for i in range(26):
                total += arr[i]
                mx = max(mx, arr[i])
            pairs = total // 2
            if total - mx < pairs:
                pairs = total - mx
            return [pairs, total - 2 * pairs]

        xx = 0
        left = [0] * 26
        right = [0] * 26
        for c in cards:
            a, b = c[0], c[1]
            if a == x and b == x:
                xx += 1
            elif a == x:
                left[ord(b) - 97] += 1
            elif b == x:
                right[ord(a) - 97] += 1
        lp = pair_group(left)
        rp = pair_group(right)
        ans = lp[0] + rp[0]
        rem = lp[1] + rp[1]
        use = min(xx, rem)
        ans += use
        xx -= use
        ans += xx // 2
        return ans
