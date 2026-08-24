# LeetCode 2305 - Fair Distribution of Cookies
# https://leetcode.com/problems/fair-distribution-of-cookies/

from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bags = [0] * k
        ans = float("inf")

        def dfs(i: int) -> None:
            nonlocal ans
            if i == len(cookies):
                mx = 0
                for b in bags:
                    mx = max(mx, b)
                ans = min(ans, mx)
                return
            seen = set()
            for j in range(len(bags)):
                if bags[j] in seen:
                    continue
                seen.add(bags[j])
                bags[j] += cookies[i]
                if bags[j] < ans:
                    dfs(i + 1)
                bags[j] -= cookies[i]
                if bags[j] == 0:
                    break

        dfs(0)
        return int(ans)
