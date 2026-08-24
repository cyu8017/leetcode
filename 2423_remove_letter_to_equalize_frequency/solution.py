# LeetCode 2423 - Remove Letter To Equalize Frequency
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        for skip in range(len(word)):
            cnt = [0] * 26
            for i, ch in enumerate(word):
                if i == skip:
                    continue
                cnt[ord(ch) - 97] += 1
            freq = {}
            for c in cnt:
                if c > 0:
                    freq[c] = freq.get(c, 0) + 1
            if len(freq) == 1:
                return True
        return False
