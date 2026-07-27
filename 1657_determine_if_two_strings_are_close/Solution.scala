// LeetCode 1657 - Determine if Two Strings Are Close
// https://leetcode.com/problems/determine-if-two-strings-are-close/

object Solution {
  def closeStrings(word1: String, word2: String): Boolean = {
    if (word1.length != word2.length) return false
    val c1 = Array.fill(26)(0)
    val c2 = Array.fill(26)(0)
    for (i <- word1.indices) {
      c1(word1(i) - 'a') += 1
      c2(word2(i) - 'a') += 1
    }
    val v1 = scala.collection.mutable.ArrayBuffer[Int]()
    val v2 = scala.collection.mutable.ArrayBuffer[Int]()
    for (i <- 0 until 26) {
      if ((c1(i) == 0) != (c2(i) == 0)) return false
      if (c1(i) > 0) {
        v1 += c1(i)
        v2 += c2(i)
      }
    }
    v1.sorted == v2.sorted
  }
}
