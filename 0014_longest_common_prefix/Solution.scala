// LeetCode 0014 - Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/

object Solution {
  def longestCommonPrefix(strs: Array[String]): String = {
    if (strs.isEmpty) {
      return ""
    }

    var i = 0
    while (i < strs(0).length) {
      val ch = strs(0)(i)
      var j = 1
      while (j < strs.length) {
        if (i >= strs(j).length || strs(j)(i) != ch) {
          return strs(0).substring(0, i)
        }
        j += 1
      }
      i += 1
    }

    strs(0)
  }
}
