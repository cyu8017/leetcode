// LeetCode 0028 - Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

object Solution {
  def strStr(haystack: String, needle: String): Int = {
    if (needle.isEmpty) {
      return 0
    }

    val needleLen = needle.length
    var i = 0
    while (i <= haystack.length - needleLen) {
      if (haystack.substring(i, i + needleLen) == needle) {
        return i
      }
      i += 1
    }

    -1
  }
}
