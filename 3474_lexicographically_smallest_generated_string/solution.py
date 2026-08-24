# LeetCode 3474 - Lexicographically Smallest Generated String
# https://leetcode.com/problems/lexicographically-smallest-generated-string/


class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        L = n + m - 1
        ans = ["?"] * L
        for i in range(n):
            if str1[i] == "T":
                for j in range(m):
                    if ans[i + j] != "?" and ans[i + j] != str2[j]:
                        return ""
                    ans[i + j] = str2[j]
        for i in range(L):
            if ans[i] == "?":
                ans[i] = "a"
        for i in range(n):
            if str1[i] == "F":
                match = True
                for j in range(m):
                    if ans[i + j] != str2[j]:
                        match = False
                        break
                if match:
                    changed = False
                    for j in range(m - 1, -1, -1):
                        pos = i + j
                        forced = False
                        for t in range(n):
                            if str1[t] == "T" and pos >= t and pos < t + m:
                                forced = True
                                break
                        if not forced:
                            ans[pos] = "b"
                            changed = True
                            break
                    if not changed:
                        return ""
        for i in range(n):
            match = True
            for j in range(m):
                if ans[i + j] != str2[j]:
                    match = False
                    break
            if str1[i] == "T" and not match:
                return ""
            if str1[i] == "F" and match:
                return ""
        return "".join(ans)
