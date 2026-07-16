// LeetCode 0245 - Shortest Word Distance III
// https://leetcode.com/problems/shortest-word-distance-iii/

object Solution {
  def shortestWordDistance(wordsDict: Array[String], word1: String, word2: String): Int = {
    if (word1 == word2) {
      var previous = -1
      var best = Int.MaxValue
      wordsDict.zipWithIndex.foreach { case (word, index) =>
        if (word == word1) {
          if (previous >= 0) best = math.min(best, index - previous)
          previous = index
        }
      }
      best
    } else {
      var index1 = -1
      var index2 = -1
      var best = Int.MaxValue
      wordsDict.zipWithIndex.foreach { case (word, index) =>
        if (word == word1) {
          index1 = index
          if (index2 >= 0) best = math.min(best, index - index2)
        }
        if (word == word2) {
          index2 = index
          if (index1 >= 0) best = math.min(best, index - index1)
        }
      }
      best
    }
  }
}
