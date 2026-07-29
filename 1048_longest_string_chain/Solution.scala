// LeetCode 1048 - Longest String Chain
// https://leetcode.com/problems/longest-string-chain/

object Solution {
  def longestStrChain(words: Array[String]): Int = {
    val sorted = words.sortBy(_.length)
    val dp = scala.collection.mutable.Map.empty[String, Int]
    var ans = 1
    for (w <- sorted) {
      dp(w) = 1
      for (i <- w.indices) {
        val prev = w.substring(0, i) + w.substring(i + 1)
        if (dp.contains(prev)) dp(w) = math.max(dp(w), dp(prev) + 1)
      }
      ans = math.max(ans, dp(w))
    }
    ans
  }
}
