// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

object Solution {
  def getLongestSubsequence(words: Array[String], groups: Array[Int]): Array[String] = {
    val ans = scala.collection.mutable.ArrayBuffer(words(0))
    var last = groups(0)
    for (i <- 1 until words.length if groups(i) != last) {
      ans += words(i)
      last = groups(i)
    }
    ans.toArray
  }
}
