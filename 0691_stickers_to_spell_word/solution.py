# LeetCode 0691 - Stickers to Spell Word
# https://leetcode.com/problems/stickers-to-spell-word/

from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        need = Counter(target)
        chars = sorted(need)
        sticks: list[Counter] = []
        for sticker in stickers:
            counts = Counter(sticker)
            useful = Counter({ch: counts[ch] for ch in need if counts[ch]})
            if useful:
                sticks.append(useful)

        @lru_cache(None)
        def dfs(state: tuple[int, ...]) -> float:
            state_list = list(state)
            i = 0
            while i < len(state_list) and state_list[i] == 0:
                i += 1
            if i == len(state_list):
                return 0

            first = chars[i]
            best = float("inf")
            for stick in sticks:
                if stick[first] == 0:
                    continue
                nxt = state_list[:]
                for j, ch in enumerate(chars):
                    nxt[j] = max(0, nxt[j] - stick[ch])
                best = min(best, 1 + dfs(tuple(nxt)))
            return best

        result = dfs(tuple(need[ch] for ch in chars))
        return -1 if result == float("inf") else int(result)
