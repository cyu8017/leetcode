// LeetCode 3088 - Make String Anti-palindrome
// https://leetcode.com/problems/make-string-anti-palindrome/

object Solution {
  def makeAntiPalindrome(s: String): String = {
    val arr = s.toCharArray.sorted
    val n = arr.length
    val m = n / 2
    if (arr(m) == arr(m - 1)) {
      var i = m
      while (i < n && arr(i) == arr(i - 1)) i += 1
      var j = m
      while (j < n && arr(j) == arr(n - j - 1)) {
        if (i >= n) return "-1"
        val tmp = arr(i)
        arr(i) = arr(j)
        arr(j) = tmp
        i += 1
        j += 1
      }
    }
    new String(arr)
  }
}
