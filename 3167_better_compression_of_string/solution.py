# LeetCode 3167 - Better Compression of String
# https://leetcode.com/problems/better-compression-of-string/


class Solution:
    def betterCompression(self, compressed: str) -> str:
        cnt = [0] * 26
        n = len(compressed)
        i = 0
        while i < n:
            c = compressed[i]
            j = i + 1
            x = 0
            while j < n:
                d = compressed[j]
                if d < "0" or d > "9":
                    break
                x = x * 10 + (ord(d) - 48)
                j += 1
            cnt[ord(c) - 97] += x
            i = j
        ans = []
        for c in range(26):
            if cnt[c] > 0:
                ans.append(chr(97 + c))
                ans.append(str(cnt[c]))
        return "".join(ans)
