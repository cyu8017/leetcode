# LeetCode 3387 - Maximize Amount After Two Days of Conversions
# https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

from typing import Dict, List


def buildRateGraph(pairs: List[List[str]], rates: List[float]) -> Dict[str, Dict[str, float]]:
    g = {}
    for i in range(len(pairs)):
        a, b = pairs[i][0], pairs[i][1]
        if a not in g:
            g[a] = {}
        if b not in g:
            g[b] = {}
        g[a][b] = rates[i]
        g[b][a] = 1.0 / rates[i]
    return g


def bellman(start: str, pairs: List[List[str]], rates: List[float]) -> Dict[str, float]:
    g = buildRateGraph(pairs, rates)
    dist = {start: 1.0}
    for _ in range(100):
        updated = False
        for frm, tos in g.items():
            if frm not in dist or dist[frm] == 0:
                continue
            for to, rate in tos.items():
                nv = dist[frm] * rate
                if to not in dist or nv > dist[to]:
                    dist[to] = nv
                    updated = True
        if not updated:
            break
    return dist


class Solution:
    def maxAmount(
        self,
        initialCurrency: str,
        pairs1: List[List[str]],
        rates1: List[float],
        pairs2: List[List[str]],
        rates2: List[float],
    ) -> float:
        amt1 = bellman(initialCurrency, pairs1, rates1)
        ans = 1.0
        g2 = buildRateGraph(pairs2, rates2)
        for c, a in amt1.items():
            if a <= 0:
                continue
            dist = {c: a}
            updated = True
            it = 0
            while it < 100 and updated:
                updated = False
                for frm, tos in g2.items():
                    if frm not in dist or dist[frm] == 0:
                        continue
                    for to, rate in tos.items():
                        nv = dist[frm] * rate
                        if to not in dist or nv > dist[to]:
                            dist[to] = nv
                            updated = True
                it += 1
            if initialCurrency in dist and dist[initialCurrency] > ans:
                ans = dist[initialCurrency]
        return ans
