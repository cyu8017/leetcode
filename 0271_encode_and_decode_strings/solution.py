# LeetCode 0271 - Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings/

from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        parts: list[str] = []
        for text in strs:
            parts.append(f"{len(text)}#{text}")
        return "".join(parts)

    def decode(self, encoded: str) -> List[str]:
        result: list[str] = []
        index = 0
        while index < len(encoded):
            delimiter = encoded.index("#", index)
            length = int(encoded[index:delimiter])
            start = delimiter + 1
            result.append(encoded[start : start + length])
            index = start + length
        return result
