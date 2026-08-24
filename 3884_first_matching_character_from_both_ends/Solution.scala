// LeetCode 3884 - First Matching Character From Both Ends
// https://leetcode.com/problems/first-matching-character-from-both-ends/

object Solution {
  def firstMatchingIndex(s: String): Int = {
    val n = s.length
    var i = 0
    while (i < n / 2 + 1) {
      if (s.charAt(i) == s.charAt(n - i - 1)) return i
      i += 1
    }
    -1
  }
}
