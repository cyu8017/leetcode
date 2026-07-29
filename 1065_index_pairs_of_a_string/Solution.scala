// LeetCode 1065 - Index Pairs of a String
// https://leetcode.com/problems/index-pairs-of-a-string/

object Solution {
  def indexPairs(text: String, words: Array[String]): Array[Array[Int]] = {
    val wordSet = words.toSet
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    val n = text.length
    for (i <- 0 until n; j <- i until n if wordSet.contains(text.substring(i, j + 1))) {
      ans += Array(i, j)
    }
    ans.toArray
  }
}
