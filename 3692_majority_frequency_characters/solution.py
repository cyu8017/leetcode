# LeetCode 3692 - Majority Frequency Characters
# https://leetcode.com/problems/majority-frequency-characters/


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        f = {}
        for i in range(26):
            if cnt[i] > 0:
                f[cnt[i]] = f.get(cnt[i], "") + chr(97 + i)
        mx = 0
        mv = 0
        ans = ""
        for v, cs in f.items():
            if len(cs) > mx or (len(cs) == mx and v > mv):
                mx = len(cs)
                mv = v
                ans = cs
        return ans
