# LeetCode 2227 - Encrypt and Decrypt Strings
# https://leetcode.com/problems/encrypt-and-decrypt-strings/

from typing import List


class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.enc = {}
        self.cnt = {}
        for i in range(len(keys)):
            self.enc[keys[i]] = values[i]
        for w in dictionary:
            e = self.encrypt(w)
            self.cnt[e] = self.cnt.get(e, 0) + 1

    def encrypt(self, word1: str) -> str:
        b = []
        for c in word1:
            if c not in self.enc:
                return ""
            b.append(self.enc[c])
        return "".join(b)

    def decrypt(self, word2: str) -> int:
        return self.cnt.get(word2, 0)
