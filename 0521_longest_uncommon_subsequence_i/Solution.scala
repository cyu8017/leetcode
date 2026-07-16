// LeetCode 0521 - Longest Uncommon Subsequence I
// https://leetcode.com/problems/longest-uncommon-subsequence-i/

object Solution {
  def findLUSlength(a: String, b: String): Int =
    if (a == b) -1 else math.max(a.length, b.length)
}
