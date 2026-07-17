// LeetCode 1754 - Largest Merge Of Two Strings
// https://leetcode.com/problems/largest-merge-of-two-strings/

object Solution {
  def largestMerge(word1: String, word2: String): String = {
    var i = 0
    var j = 0
    val out = new StringBuilder
    while (i < word1.length && j < word2.length) {
      if (word1.substring(i) > word2.substring(j)) {
        out.append(word1.charAt(i))
        i += 1
      } else {
        out.append(word2.charAt(j))
        j += 1
      }
    }
    out.append(word1.substring(i))
    out.append(word2.substring(j))
    out.toString
  }
}
