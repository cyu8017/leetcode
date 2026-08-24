# LeetCode 3163 - String Compression III
# https://leetcode.com/problems/string-compression-iii/


class Solution:
    def compressedString(self, word: str) -> str:
        ans = []
        n = len(word)
        i = 0
        while i < n:
            j = i + 1
            while j < n and word[j] == word[i]:
                j += 1
            k = j - i
            while k > 0:
                x = min(9, k)
                ans.append(str(x))
                ans.append(word[i])
                k -= x
            i = j
        return "".join(ans)
