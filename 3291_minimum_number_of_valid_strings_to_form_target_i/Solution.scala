// LeetCode 3291 - Minimum Number of Valid Strings to Form Target I
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/

object Solution {
  private class TrieNode {
    val next = new Array[TrieNode](26)
  }

  def minValidStrings(words: Array[String], target: String): Int = {
    val n = target.length
    val inf = 1000000000
    val dp = Array.fill(n + 1)(inf)
    dp(0) = 0
    val root = new TrieNode
    for (w <- words) {
      var cur = root
      for (c <- w) {
        val ci = c - 'a'
        if (cur.next(ci) == null) cur.next(ci) = new TrieNode
        cur = cur.next(ci)
      }
    }
    var i = 0
    while (i < n) {
      if (dp(i) != inf) {
        var cur = root
        var j = i
        while (j < n) {
          val ci = target.charAt(j) - 'a'
          if (cur.next(ci) == null) { j = n }
          else {
            cur = cur.next(ci)
            if (dp(i) + 1 < dp(j + 1)) dp(j + 1) = dp(i) + 1
            j += 1
          }
        }
      }
      i += 1
    }
    if (dp(n) == inf) -1 else dp(n)
  }
}
