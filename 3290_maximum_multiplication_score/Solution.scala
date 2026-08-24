// LeetCode 3290 - Maximum Multiplication Score
// https://leetcode.com/problems/maximum-multiplication-score/

object Solution {
  def maxScore(a: Array[Int], b: Array[Int]): Long = {
    val neg = -(1L << 62)
    val dp = Array(0L, neg, neg, neg, neg)
    for (x <- b) {
      var k = 4
      while (k >= 1) {
        if (dp(k - 1) != neg) {
          val v = dp(k - 1) + a(k - 1).toLong * x
          if (v > dp(k)) dp(k) = v
        }
        k -= 1
      }
    }
    dp(4)
  }
}
