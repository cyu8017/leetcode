# LeetCode 0291 - Word Pattern II
# https://leetcode.com/problems/word-pattern-ii/


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(pattern_index: int, string_index: int) -> bool:
            if pattern_index == len(pattern):
                return string_index == len(s)
            char = pattern[pattern_index]
            if char in char_to_word:
                word = char_to_word[char]
                if not s.startswith(word, string_index):
                    return False
                return backtrack(pattern_index + 1, string_index + len(word))
            for end in range(string_index + 1, len(s) + 1):
                word = s[string_index:end]
                if word in word_to_char:
                    continue
                char_to_word[char] = word
                word_to_char[word] = char
                if backtrack(pattern_index + 1, end):
                    return True
                del char_to_word[char]
                del word_to_char[word]
            return False

        char_to_word: dict[str, str] = {}
        word_to_char: dict[str, str] = {}
        return backtrack(0, 0)
