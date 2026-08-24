// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

object Solution {
  def makeSmallestPalindrome(s: String): String = {
    val arr = s.toCharArray
    val n = arr.length
    var i = 0
    while (i < n / 2) {
      val c = if (arr(i) < arr(n - 1 - i)) arr(i) else arr(n - 1 - i)
      arr(i) = c
      arr(n - 1 - i) = c
      i += 1
    }
    new String(arr)
  }
}
