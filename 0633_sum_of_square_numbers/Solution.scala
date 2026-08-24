// LeetCode 0633 - Sum of Square Numbers
// https://leetcode.com/problems/sum-of-square-numbers/

object Solution {
  def judgeSquareSum(c: Int): Boolean = {
    var left = 0L
    var right = math.sqrt(c.toDouble).toLong
    while (left <= right) {
      val total = left * left + right * right
      if (total == c) return true
      if (total < c) left += 1 else right -= 1
    }
    false
  }
}
