# LeetCode 0471 - Encode String with Shortest Length
# https://leetcode.com/problems/encode-string-with-shortest-length/


class Solution:
    def encode(self, s: str) -> str:
        length = len(s)
        dp = [""] * (length + 1)

        def encode_word(word: str) -> str:
            size = len(word)
            best = word
            for unit_length in range(1, size // 2 + 1):
                if size % unit_length != 0:
                    continue
                unit = word[:unit_length]
                if unit * (size // unit_length) == word:
                    encoded = f"{size // unit_length}[{unit}]"
                    if len(encoded) < len(best) or (
                        len(encoded) == len(best) and encoded < best
                    ):
                        best = encoded
            return best

        for index in range(1, length + 1):
            dp[index] = encode_word(s[:index])
            for split in range(1, index):
                candidate = dp[index - split] + encode_word(s[index - split : index])
                if len(candidate) < len(dp[index]) or (
                    len(candidate) == len(dp[index]) and candidate < dp[index]
                ):
                    dp[index] = candidate
        return dp[length]
