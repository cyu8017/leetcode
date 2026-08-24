// LeetCode 0680 - Valid Palindrome II
// https://leetcode.com/problems/valid-palindrome-ii/

object Solution {
  def validPalindrome(s: String): Boolean = {
    def isPalindrome(left0: Int, right0: Int): Boolean = {
      var left = left0
      var right = right0
      while (left < right) {
        if (s.charAt(left) != s.charAt(right)) return false
        left += 1
        right -= 1
      }
      true
    }
    var left = 0
    var right = s.length - 1
    while (left < right) {
      if (s.charAt(left) != s.charAt(right)) {
        return isPalindrome(left + 1, right) || isPalindrome(left, right - 1)
      }
      left += 1
      right -= 1
    }
    true
  }
}
