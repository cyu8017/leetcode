// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

object Solution {
  def getWordsInLongestSubsequence(words: Array[String], groups: Array[Int]): Array[String] = {
    val n = words.length
    val dp = Array.fill(n)(1)
    val prev = Array.fill(n)(-1)
    var best = 1
    var bestI = 0
    for (i <- 0 until n) {
      for (j <- 0 until i) {
        if (groups(i) != groups(j) && hamming(words(i), words(j)) == 1 && dp(j) + 1 > dp(i)) {
          dp(i) = dp(j) + 1
          prev(i) = j
        }
      }
      if (dp(i) > best) {
        best = dp(i)
        bestI = i
      }
    }
    val path = scala.collection.mutable.ArrayBuffer.empty[String]
    var i = bestI
    while (i != -1) {
      path += words(i)
      i = prev(i)
    }
    path.reverse.toArray
  }

  private def hamming(a: String, b: String): Int = {
    if (a.length != b.length) return 100
    var d = 0
    for (i <- a.indices if a.charAt(i) != b.charAt(i)) d += 1
    d
  }
}
