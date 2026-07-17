// LeetCode 1774 - Closest Dessert Cost
// https://leetcode.com/problems/closest-dessert-cost/

class Solution {
    private var best = 0
    private var target = 0
    private lateinit var toppingCosts: IntArray

    fun closestCost(baseCosts: IntArray, toppingCosts: IntArray, target: Int): Int {
        this.best = Int.MAX_VALUE / 2
        this.target = target
        this.toppingCosts = toppingCosts
        for (base in baseCosts) {
            dfs(0, base)
        }
        return best
    }

    private fun dfs(i: Int, cur: Int) {
        val curDiff = Math.abs(cur - target)
        val bestDiff = Math.abs(best - target)
        if (curDiff < bestDiff || (curDiff == bestDiff && cur < best)) {
            best = cur
        }
        if (i == toppingCosts.size || cur >= target) {
            return
        }
        dfs(i + 1, cur)
        dfs(i + 1, cur + toppingCosts[i])
        dfs(i + 1, cur + 2 * toppingCosts[i])
    }
}
