// LeetCode 3998 - Transform Binary String Using Subsequence Sort
// https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/

object Solution {
  def transformStr(s: String, strs: Array[String]): Array[Boolean] = {
    val n = s.length
    val prefix = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + (if (s.charAt(i) == '1') 1 else 0)
      i += 1
    }
    val result = new Array[Boolean](strs.length)
    i = 0
    while (i < strs.length) {
      var left = 0
      var right = 0
      var ok = true
      var j = 0
      while (j < n && ok) {
        left += (if (strs(i).charAt(j) == '1') 1 else 0)
        val add = if (strs(i).charAt(j) != '0') 1 else 0
        right = right + add
        if (right > prefix(j + 1)) right = prefix(j + 1)
        if (left > right) ok = false
        j += 1
      }
      result(i) = ok && left <= prefix(n) && prefix(n) <= right
      i += 1
    }
    result
  }
}
