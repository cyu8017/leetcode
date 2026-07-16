// LeetCode 0265 - Paint House II
// https://leetcode.com/problems/paint-house-ii/

object Solution {
  def minCostII(costs: Array[Array[Int]]): Int = {
    if (costs.isEmpty) {
      return 0
    }
    val colorCount = costs(0).length
    var previous = costs(0).clone()
    for (row <- 1 until costs.length) {
      val minCost = previous.min
      val minIndex = previous.indexOf(minCost)
      val secondMin = previous.zipWithIndex.collect {
        case (value, index) if index != minIndex => value
      }.min
      val current = Array.fill(colorCount)(0)
      for (color <- 0 until colorCount) {
        val extra = if (color == minIndex) secondMin else minCost
        current(color) = costs(row)(color) + extra
      }
      previous = current
    }
    previous.min
  }
}
