// LeetCode 0009 - Palindrome Number
// https://leetcode.com/problems/palindrome-number/

object Solution {
  def isPalindrome(x: Int): Boolean = {
    if (x < 0 || (x != 0 && x % 10 == 0)) {
      return false
    }

    var value = x
    var reversedHalf = 0
    while (value > reversedHalf) {
      reversedHalf = reversedHalf * 10 + value % 10
      value /= 10
    }

    value == reversedHalf || value == reversedHalf / 10
  }
}
