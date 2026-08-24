// LeetCode 0746 - Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/

object Solution {
  def minCostClimbingStairs(cost: Array[Int]): Int = {
    var a = 0
    var b = 0
    var i = cost.length - 1
    while (i >= 0) {
      val nextA = cost(i) + math.min(a, b)
      b = a
      a = nextA
      i -= 1
    }
    math.min(a, b)
  }
}
