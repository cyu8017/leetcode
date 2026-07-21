// LeetCode 1802 - Maximum Value at a Given Index in a Bounded Array
// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

object Solution {
  def maxValue(n: Int, index: Int, maxSum: Int): Int = {
    def minSideSum(value: Long, count: Long): Long = {
      if (value > count) (value - 1 + value - count) * count / 2
      else value * (value - 1) / 2 + (count - value + 1)
    }

    var lo = 1
    var hi = maxSum
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      val total = minSideSum(mid, index) + mid + minSideSum(mid, n - index - 1)
      if (total <= maxSum) lo = mid else hi = mid - 1
    }
    lo
  }
}
