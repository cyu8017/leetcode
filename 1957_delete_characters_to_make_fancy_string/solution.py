class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        for c in s:
            if len(ans) >= 2 and ans[-1] == c and ans[-2] == c:
                continue
            ans.append(c)
        return ''.join(ans)
