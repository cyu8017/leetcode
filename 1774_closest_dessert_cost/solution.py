class Solution:
    def closestCost(self, baseCosts, toppingCosts, target):
        sums = {0}
        for cost in toppingCosts:
            nxt = set(sums)
            for s in sums:
                x = s + cost
                while x not in nxt:
                    nxt.add(x)
                    x += cost
            sums = nxt
        best = float("inf")
        for base in baseCosts:
            for top in sums:
                total = base + top
                if abs(total - target) < abs(best - target) or (
                    abs(total - target) == abs(best - target) and total < best
                ):
                    best = total
        return best
