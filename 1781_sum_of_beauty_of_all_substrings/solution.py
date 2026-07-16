class Solution:
    def beautySum(self, s):
        ans = 0
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)):
                freq[ord(s[j]) - 97] += 1
                lo = min(x for x in freq if x)
                hi = max(freq)
                ans += hi - lo
        return ans
