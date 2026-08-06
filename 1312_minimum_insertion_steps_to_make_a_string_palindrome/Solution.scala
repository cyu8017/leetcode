// LeetCode 1312 - Minimum Insertion Steps To Make A String Palindrome
// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

object Solution {
  def minInsertions(s: String): Int = {
    val n = s.length
    val dp = Array.ofDim[Int](n)
    for (left <- n - 2 to 0 by -1) {
      var diagonal = 0
      for (right <- left + 1 until n) {
        val old = dp(right)
        dp(right) =
          if (s(left) == s(right)) diagonal
          else 1 + math.min(dp(right), dp(right - 1))
        diagonal = old
      }
    }
    if (dp.isEmpty) 0 else dp(n - 1)
  }
}
