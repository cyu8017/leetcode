// LeetCode 1858 - Longest Word With All Prefixes
// https://leetcode.com/problems/longest-word-with-all-prefixes/

object Solution {
  def longestWord(words: Array[String]): String = {
    val wordSet = words.toSet
    var best = ""
    for (word <- words) {
      var prefix = word
      var valid = true
      while (prefix.nonEmpty && valid) {
        if (!wordSet.contains(prefix)) valid = false
        else prefix = prefix.substring(0, prefix.length - 1)
      }
      if (valid && (word.length > best.length || (word.length == best.length && word < best))) {
        best = word
      }
    }
    best
  }
}
