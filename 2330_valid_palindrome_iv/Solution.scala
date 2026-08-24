// LeetCode 2330 - Valid Palindrome IV
// https://leetcode.com/problems/valid-palindrome-iv/

object Solution {
  def makePalindrome(s: String): Boolean = {
    var diff = 0
    var i = 0
    var j = s.length - 1
    while (i < j) {
      if (s.charAt(i) != s.charAt(j)) {
        diff += 1
        if (diff > 2) return false
      }
      i += 1
      j -= 1
    }
    true
  }
}
