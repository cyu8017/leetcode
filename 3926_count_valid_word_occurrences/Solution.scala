// LeetCode 3926 - Count Valid Word Occurrences
// https://leetcode.com/problems/count-valid-word-occurrences/

import scala.collection.mutable

object Solution {
  def countWordOccurrences(chunks: Array[String], queries: Array[String]): Array[Int] = {
    val s = chunks.mkString
    val n = s.length
    val cnt = mutable.HashMap.empty[String, Int]
    var i = 0
    while (i < n) {
      if (s.charAt(i) == ' ' || s.charAt(i) == '-') {
        i += 1
      } else {
        var j = i
        while (
          j < n && s.charAt(j) != ' ' &&
            (s.charAt(j) != '-' || (j + 1 < n && s.charAt(j + 1) != ' ' && s.charAt(j + 1) != '-'))
        ) {
          j += 1
        }
        val word = s.substring(i, j)
        cnt(word) = cnt.getOrElse(word, 0) + 1
        i = j
      }
    }
    val ans = new Array[Int](queries.length)
    var k = 0
    while (k < queries.length) {
      ans(k) = cnt.getOrElse(queries(k), 0)
      k += 1
    }
    ans
  }
}
