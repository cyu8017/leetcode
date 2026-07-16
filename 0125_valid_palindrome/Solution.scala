// LeetCode 0125 - Valid Palindrome
// https://leetcode.com/problems/valid-palindrome/

object Solution {
  def isPalindrome(s: String): Boolean = {
    var left = 0
    var right = s.length - 1
    while (left < right) {
      while (left < right && !Character.isLetterOrDigit(s.charAt(left))) left += 1
      while (left < right && !Character.isLetterOrDigit(s.charAt(right))) right -= 1
      if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) return false
      left += 1
      right -= 1
    }
    true
  }
}