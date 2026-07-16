from typing import List

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank = [{friend: i for i, friend in enumerate(pref)} for pref in preferences]
        partner = {}
        for a, b in pairs:
            partner[a], partner[b] = b, a
        unhappy = 0
        for x in range(n):
            y = partner[x]
            if any(rank[u][x] < rank[u][partner[u]] for u in preferences[x][:rank[x][y]]):
                unhappy += 1
        return unhappy
