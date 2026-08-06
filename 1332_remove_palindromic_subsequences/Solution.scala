// LeetCode 1332 - Remove Palindromic Subsequences
// https://leetcode.com/problems/remove-palindromic-subsequences/

object Solution {
  def removePalindromeSub(s: String): Int = {
    if (s.isEmpty) return 0
    var i = 0
    var j = s.length - 1
    while (i < j) {
      if (s(i) != s(j)) return 2
      i += 1
      j -= 1
    }
    1
  }
}
