// LeetCode 1770 - Maximum Score from Performing Multiplication Operations
// https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

object Solution {
  def maximumScore(nums: Array[Int], multipliers: Array[Int]): Int = {
    val n = nums.length
    val m = multipliers.length
    var next = new Array[Int](m + 1)
    for (i <- (m - 1) to 0 by -1) {
      val cur = new Array[Int](m + 1)
      for (left <- i to 0 by -1) {
        val right = n - 1 - (i - left)
        val takeLeft = nums(left) * multipliers(i) + next(left + 1)
        val takeRight = nums(right) * multipliers(i) + next(left)
        cur(left) = math.max(takeLeft, takeRight)
      }
      next = cur
    }
    next(0)
  }
}
