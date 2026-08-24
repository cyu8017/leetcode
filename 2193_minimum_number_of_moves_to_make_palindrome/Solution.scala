// LeetCode 2193 - Minimum Number of Moves to Make Palindrome
// https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

object Solution {
  def minMovesToMakePalindrome(s: String): Int = {
    val b = new StringBuilder(s)
    var ans = 0
    while (b.length > 1) {
      var j = b.length - 1
      while (j > 0 && b.charAt(j) != b.charAt(0)) j -= 1
      if (j == 0) {
        ans += b.length / 2
        b.deleteCharAt(0)
      } else {
        ans += b.length - 1 - j
        b.deleteCharAt(j)
        b.deleteCharAt(0)
      }
    }
    ans
  }
}
