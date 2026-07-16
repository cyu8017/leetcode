MOD = 1_000_000_007
class Solution:
    def countHomogenous(self, s):
        ans = 0
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            length = j - i
            ans = (ans + length * (length + 1) // 2) % MOD
            i = j
        return ans
