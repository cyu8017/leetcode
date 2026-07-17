class Solution:
    def closestCost(self, baseCosts, toppingCosts, target):
        best = float("inf")

        def dfs(i, cur):
            nonlocal best
            if abs(cur - target) < abs(best - target) or (
                abs(cur - target) == abs(best - target) and cur < best
            ):
                best = cur
            if i == len(toppingCosts) or cur >= target:
                return
            dfs(i + 1, cur)
            dfs(i + 1, cur + toppingCosts[i])
            dfs(i + 1, cur + 2 * toppingCosts[i])

        for base in baseCosts:
            dfs(0, base)
        return best
