// LeetCode 1774 - Closest Dessert Cost
// https://leetcode.com/problems/closest-dessert-cost/

object Solution {
  def closestCost(baseCosts: Array[Int], toppingCosts: Array[Int], target: Int): Int = {
    var best = Int.MaxValue / 2

    def dfs(i: Int, cur: Int): Unit = {
      val curDiff = math.abs(cur - target)
      val bestDiff = math.abs(best - target)
      if (curDiff < bestDiff || (curDiff == bestDiff && cur < best)) {
        best = cur
      }
      if (i == toppingCosts.length || cur >= target) {
        return
      }
      dfs(i + 1, cur)
      dfs(i + 1, cur + toppingCosts(i))
      dfs(i + 1, cur + 2 * toppingCosts(i))
    }

    for (base <- baseCosts) {
      dfs(0, base)
    }
    best
  }
}
