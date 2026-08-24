// LeetCode 3838 - Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/

object Solution {
  def mapWordWeights(words: Array[String], weights: Array[Int]): String = {
    val ans = new StringBuilder
    words.foreach { w =>
      var s = 0
      w.foreach { c => s = (s + weights(c - 'a')) % 26 }
      ans.append(('a' + (25 - s)).toChar)
    }
    ans.toString
  }
}
