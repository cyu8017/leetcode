// LeetCode 2240 - Number of Ways to Buy Pens and Pencils
// https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

object Solution {
  def waysToBuyPensPencils(total: Int, cost1: Int, cost2: Int): Long = {
    var ans = 0L
    var pens = 0
    while (pens.toLong * cost1 <= total) {
      val remain = total - pens * cost1
      ans += remain / cost2 + 1
      pens += 1
    }
    ans
  }
}
