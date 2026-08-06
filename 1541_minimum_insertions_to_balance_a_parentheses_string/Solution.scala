// LeetCode 1541 - Minimum Insertions to Balance a Parentheses String
// https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

object Solution {
  def minInsertions(s: String): Int = {
    var insertions = 0
    var needed = 0
    var i = 0
    while (i < s.length) {
      if (s(i) == '(') {
        needed += 2
        if ((needed & 1) == 1) {
          insertions += 1
          needed -= 1
        }
      } else {
        needed -= 1
        if (needed < 0) {
          insertions += 1
          needed = 1
        }
      }
      i += 1
    }
    insertions + needed
  }
}
