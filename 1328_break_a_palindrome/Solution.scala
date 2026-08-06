// LeetCode 1328 - Break a Palindrome
// https://leetcode.com/problems/break-a-palindrome/

object Solution {
  def breakPalindrome(palindrome: String): String = {
    if (palindrome.length == 1) return ""
    val chars = palindrome.toCharArray
    for (i <- 0 until chars.length / 2) {
      if (chars(i) != 'a') {
        chars(i) = 'a'
        return new String(chars)
      }
    }
    chars(chars.length - 1) = 'b'
    new String(chars)
  }
}
