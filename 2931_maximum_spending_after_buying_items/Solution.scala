// LeetCode 2931 - Maximum Spending After Buying Items
// https://leetcode.com/problems/maximum-spending-after-buying-items/

object Solution {
  def maxSpending(values: Array[Array[Int]]): Long = {
    val m = values.length
    val n = values(0).length
    val idx = Array.fill(m)(n - 1)
    var ans = 0L
    var day = 1L
    val total = m * n
    for (_ <- 0 until total) {
      var bestI = -1
      var bestV = 1L << 60
      for (i <- 0 until m) {
        if (idx(i) >= 0 && values(i)(idx(i)) < bestV) {
          bestV = values(i)(idx(i))
          bestI = i
        }
      }
      ans += bestV * day
      idx(bestI) -= 1
      day += 1
    }
    ans
  }
}
