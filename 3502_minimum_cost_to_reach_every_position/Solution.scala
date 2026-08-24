// LeetCode 3502 - Minimum Cost to Reach Every Position
// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

object Solution {
  def minCosts(cost: Array[Int]): Array[Int] = {
    val n = cost.length
    val ans = new Array[Int](n)
    var mi = cost(0)
    var i = 0
    while (i < n) {
      mi = math.min(mi, cost(i))
      ans(i) = mi
      i += 1
    }
    ans
  }
}
