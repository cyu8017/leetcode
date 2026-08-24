// LeetCode 3983 - Subsequence After One Replacement
// https://leetcode.com/problems/subsequence-after-one-replacement/

object Solution {
  def canMakeSubsequence(s: String, t: String): Boolean = {
    val m = s.length
    val n = t.length
    var i0 = 0
    var i1 = 0
    var j = 0
    while (i1 < m && j < n) {
      if (s.charAt(i1) == t.charAt(j)) i1 += 1
      if (i1 < i0 + 1) i1 = i0 + 1
      if (s.charAt(i0) == t.charAt(j)) i0 += 1
      j += 1
    }
    i1 == m
  }
}
