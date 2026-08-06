// LeetCode 1940 - Longest Common Subsequence Between Sorted Arrays
// https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/

object Solution {
  def longestCommonSubsequence(arrays: Array[Array[Int]]): List[Int] = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int].withDefaultValue(0)
    for (arr <- arrays; x <- arr) cnt(x) += 1
    val m = arrays.length
    arrays(0).filter(x => cnt(x) == m).toList
  }
}
