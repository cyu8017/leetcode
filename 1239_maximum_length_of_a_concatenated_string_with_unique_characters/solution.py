class Solution:
    def maxLength(self, arr: list[str]) -> int:
        masks = [(0, 0)]
        for word in arr:
            mask = 0
            for ch in word: mask |= 1 << (ord(ch) - 97)
            if mask.bit_count() != len(word): continue
            masks += [(used | mask, length + len(word)) for used, length in masks if not used & mask]
        return max(length for _, length in masks)
