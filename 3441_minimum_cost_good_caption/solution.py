# LeetCode 3441 - Minimum Cost Good Caption
# https://leetcode.com/problems/minimum-cost-good-caption/


class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""
        ans = list(caption)
        i = 0
        while i < n:
            j = i
            while j < n and ans[j] == ans[i]:
                j += 1
            if j - i >= 3:
                i = j
                continue
            need = 3 - (j - i)
            if j + need <= n:
                for t in range(need):
                    ans[j + t] = ans[i]
                i = j + need
            else:
                ch = "a"
                if i > 0:
                    ch = ans[i - 1]
                elif j < n:
                    ch = caption[j]
                for t in range(i, n):
                    ans[t] = ch
                break
        i = 0
        while i < n:
            j = i
            while j < n and ans[j] == ans[i]:
                j += 1
            if j - i < 3:
                return ""
            i = j
        return "".join(ans)
