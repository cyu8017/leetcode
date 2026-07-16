# LeetCode 0030 - Substring with Concatenation of All Words
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not words or not s:
            return []

        word_len = len(words[0])
        word_count = len(words)
        need = Counter(words)
        result: list[int] = []

        for start in range(word_len):
            left = start
            counts: Counter[str] = Counter()
            used = 0

            for right in range(start, len(s) - word_len + 1, word_len):
                word = s[right : right + word_len]
                if word not in need:
                    counts.clear()
                    used = 0
                    left = right + word_len
                    continue

                counts[word] += 1
                used += 1
                while counts[word] > need[word]:
                    left_word = s[left : left + word_len]
                    counts[left_word] -= 1
                    used -= 1
                    left += word_len

                if used == word_count:
                    result.append(left)

        return sorted(result)
