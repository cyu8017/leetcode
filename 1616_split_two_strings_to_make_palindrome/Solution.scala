// LeetCode 1616 - Split Two Strings to Make Palindrome
// https://leetcode.com/problems/split-two-strings-to-make-palindrome/

object Solution {
  def checkPalindromeFormation(a: String, b: String): Boolean = {
    def isPal(s: String, i: Int, j: Int): Boolean = {
      var lo = i
      var hi = j
      while (lo < hi) {
        if (s.charAt(lo) != s.charAt(hi)) return false
        lo += 1
        hi -= 1
      }
      true
    }
    def check(x: String, y: String): Boolean = {
      var i = 0
      var j = x.length - 1
      while (i < j && x.charAt(i) == y.charAt(j)) {
        i += 1
        j -= 1
      }
      isPal(x, i, j) || isPal(y, i, j)
    }
    check(a, b) || check(b, a)
  }
}
