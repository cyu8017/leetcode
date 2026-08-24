// LeetCode 0720 - Longest Word in Dictionary
// https://leetcode.com/problems/longest-word-in-dictionary/

object Solution {
  def longestWord(words: Array[String]): String = {
    val arr = words.clone()
    scala.util.Sorting.quickSort(arr)
    val built = scala.collection.mutable.HashSet("")
    var best = ""
    for (word <- arr) {
      if (built.contains(word.substring(0, word.length - 1))) {
        built += word
        if (word.length > best.length) best = word
      }
    }
    best
  }
}
