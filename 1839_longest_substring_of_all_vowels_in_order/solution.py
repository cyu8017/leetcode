# LeetCode 1839 - Longest Substring Of All Vowels in Order
# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = "aeiou"
        best = 0

        for start, ch in enumerate(word):
            if ch != "a":
                continue

            counts = [0] * 5
            for end in range(start, len(word)):
                current = word[end]
                if end > start and current < word[end - 1]:
                    break

                idx = vowels.index(current)
                counts[idx] += 1
                if idx > 0 and counts[idx - 1] == 0:
                    break
                if all(count > 0 for count in counts):
                    best = max(best, end - start + 1)

        return best
