// LeetCode 1768 - Merge Strings Alternately
// https://leetcode.com/problems/merge-strings-alternately/

object Solution {
  def mergeAlternately(word1: String, word2: String): String = {
    val out = new StringBuilder
    var i = 0
    var j = 0
    while (i < word1.length || j < word2.length) {
      if (i < word1.length) {
        out.append(word1(i))
        i += 1
      }
      if (j < word2.length) {
        out.append(word2(j))
        j += 1
      }
    }
    out.toString
  }
}
