// LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

object Solution {
  def canMakeSubsequence(str1: String, str2: String): Boolean = {
    var j = 0
    var i = 0
    while (i < str1.length && j < str2.length) {
      val a = str1.charAt(i)
      val b = str2.charAt(j)
      if (a == b || (a - 'a' + 1) % 26 == (b - 'a')) j += 1
      i += 1
    }
    j == str2.length
  }
}
