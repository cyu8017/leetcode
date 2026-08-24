// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/

object Solution {
  def minExtraChar(s: String, dictionary: Array[String]): Int = {
    val dict = dictionary.toSet
    val n = s.length
    val dp = Array.fill(n + 1)(n)
    dp(0) = 0
    var i = 0
    while (i < n) {
      dp(i + 1) = math.min(dp(i + 1), dp(i) + 1)
      var j = i + 1
      while (j <= n) {
        if (dict.contains(s.substring(i, j)))
          dp(j) = math.min(dp(j), dp(i))
        j += 1
      }
      i += 1
    }
    dp(n)
  }
}
