# LeetCode 0482 - License Key Formatting
# https://leetcode.com/problems/license-key-formatting/

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = [ch.upper() for ch in s if ch != "-"]
        if not chars:
            return ""
        first_len = len(chars) % k or k
        parts = ["".join(chars[:first_len])]
        for i in range(first_len, len(chars), k):
            parts.append("".join(chars[i : i + k]))
        return "-".join(parts)
