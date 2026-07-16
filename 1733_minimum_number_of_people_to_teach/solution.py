from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        known = [set(items) for items in languages]
        need = set()
        for u, v in friendships:
            if known[u - 1].isdisjoint(known[v - 1]):
                need.add(u - 1)
                need.add(v - 1)
        if not need:
            return 0
        return min(sum(lang not in known[user] for user in need) for lang in range(1, n + 1))
