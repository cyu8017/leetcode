# LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
# https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        n = len(s)
        ans = [""] * n

        def dfs(pos: int, greater: bool) -> bool:
            if pos == n:
                return greater
            start = 0 if greater else (ord(target[pos]) - 97)
            for c in range(start, 26):
                if cnt[c] == 0:
                    continue
                cnt[c] -= 1
                ans[pos] = chr(97 + c)
                ng = greater or c > (ord(target[pos]) - 97)
                if dfs(pos + 1, ng):
                    return True
                cnt[c] += 1
            return False

        if dfs(0, False):
            return "".join(ans)
        return ""
