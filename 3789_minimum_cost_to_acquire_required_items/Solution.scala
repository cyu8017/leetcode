// LeetCode 3789 - Minimum Cost To Acquire Required Items
// https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

object Solution {
  def minimumCost(cost1: Int, cost2: Int, costBoth: Int, need1: Int, need2: Int): Long = {
    val a = need1.toLong * cost1 + need2.toLong * cost2
    val b = costBoth.toLong * math.max(need1, need2)
    val mn = math.min(need1, need2)
    val c = costBoth.toLong * mn + (need1 - mn).toLong * cost1 + (need2 - mn).toLong * cost2
    math.min(a, math.min(b, c))
  }
}
