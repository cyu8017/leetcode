// LeetCode 0256 - Paint House
// https://leetcode.com/problems/paint-house/

object Solution {
  def minCost(costs: Array[Array[Int]]): Int = {
    if (costs.isEmpty) {
      0
    } else {
      var previous = costs(0).clone()
      for (row <- 1 until costs.length) {
        previous = Array(
          costs(row)(0) + math.min(previous(1), previous(2)),
          costs(row)(1) + math.min(previous(0), previous(2)),
          costs(row)(2) + math.min(previous(0), previous(1)),
        )
      }
      previous.min
    }
  }
}
