// LeetCode 1092 - Shortest Common Supersequence
// https://leetcode.com/problems/shortest-common-supersequence/

object Solution {
  def shortestCommonSupersequence(str1: String, str2: String): String = {
    val m = str1.length
    val n = str2.length
    val dp = Array.fill(m + 1, n + 1)(0)
    for (i <- 1 to m; j <- 1 to n) {
      if (str1(i - 1) == str2(j - 1)) dp(i)(j) = dp(i - 1)(j - 1) + 1
      else dp(i)(j) = math.max(dp(i - 1)(j), dp(i)(j - 1))
    }
    var i = m
    var j = n
    val chars = scala.collection.mutable.ArrayBuffer.empty[Char]
    while (i > 0 && j > 0) {
      if (str1(i - 1) == str2(j - 1)) {
        chars += str1(i - 1); i -= 1; j -= 1
      } else if (dp(i - 1)(j) >= dp(i)(j - 1)) {
        chars += str1(i - 1); i -= 1
      } else {
        chars += str2(j - 1); j -= 1
      }
    }
    while (i > 0) { chars += str1(i - 1); i -= 1 }
    while (j > 0) { chars += str2(j - 1); j -= 1 }
    chars.reverse.mkString
  }
}
