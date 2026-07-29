// LeetCode 1029 - Two City Scheduling
// https://leetcode.com/problems/two-city-scheduling/

object Solution {
  def twoCitySchedCost(costs: Array[Array[Int]]): Int = {
    val sorted = costs.sortBy(c => c(0) - c(1))
    val n = sorted.length / 2
    sorted.take(n).map(_(0)).sum + sorted.drop(n).map(_(1)).sum
  }
}
