# LeetCode 3775 - Reverse Words with Same Vowel Count
# https://leetcode.com/problems/reverse-words-with-same-vowel-count/

class Solution:
    def reverseWords(self, s: str) -> str:
        def calc(w: str) -> int:
            cnt = 0
            for c in w:
                if c in "aeiou":
                    cnt += 1
            return cnt

        words = s.strip().split()
        cnt = calc(words[0])
        ans = words[0]
        for i in range(1, len(words)):
            w = words[i]
            if calc(w) == cnt:
                w = w[::-1]
            ans += " " + w
        return ans
