// LeetCode 0524 - Longest Word in Dictionary through Deleting
// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

object Solution {
  def findLongestWord(s: String, dictionary: List[String]): String = {
    var best = ""
    for (word <- dictionary if isSubsequence(word, s)) {
      if (word.length > best.length || (word.length == best.length && word < best)) {
        best = word
      }
    }
    best
  }

  private def isSubsequence(word: String, source: String): Boolean = {
    var index = 0
    for (char <- source if index < word.length && word(index) == char) {
      index += 1
    }
    index == word.length
  }
}
