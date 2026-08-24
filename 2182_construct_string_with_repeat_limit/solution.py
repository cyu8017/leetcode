# LeetCode 2182 - Construct String With Repeat Limit
# https://leetcode.com/problems/construct-string-with-repeat-limit/
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [0] * (26)
        for i in range(len(s)):
            freq[ord(s[i]) - 97] += 1
        ans = []
        while True:
            placed = False
            for c in range(25, (0) - 1, -1):
                if freq[c] == 0:
                    continue
                if len(ans) > 0 and ord(ans[len(ans) - 1][0]) - 97 == c:
                    found = False
                    for d in range(c - 1, (0) - 1, -1):
                        if freq[d] > 0:
                            ans.append(chr(97 + d))
                            freq[d] -= 1
                            found = placed = True
                            break
                    if not found:
                        return "".join(ans)
                    break
                use = min(freq[c], repeatLimit)
                for i in range(use):
                    ans.append(chr(97 + c))
                freq[c] -= use
                placed = True
                break
            if not placed:
                break
        return "".join(ans)
