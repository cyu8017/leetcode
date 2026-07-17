// LeetCode 1798 - Maximum Number of Consecutive Values You Can Make
// https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

object Solution {
  def getMaximumConsecutive(coins: Array[Int]): Int = {
    val sorted = coins.sorted
    var reach = 0L
    var i = 0
    while (i < sorted.length && sorted(i) <= reach + 1) {
      reach += sorted(i)
      i += 1
    }
    (reach + 1).toInt
  }
}
