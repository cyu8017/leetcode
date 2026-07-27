// LeetCode 1639 - Number of Ways to Form a Target String Given a Dictionary
// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

object Solution {
  def numWays(words: Array[String], target: String): Int = {
    val MOD = 1000000007
    val m = words(0).length
    val dp = Array.fill(target.length + 1)(0L)
    dp(0) = 1L
    for (j <- 0 until m) {
      val count = Array.fill(26)(0)
      for (word <- words) count(word.charAt(j) - 'a') += 1
      var i = math.min(j + 1, target.length)
      while (i >= 1) {
        dp(i) = (dp(i) + dp(i - 1) * count(target.charAt(i - 1) - 'a')) % MOD
        i -= 1
      }
    }
    dp(target.length).toInt
  }
}
