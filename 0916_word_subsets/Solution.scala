// LeetCode 0916 - Word Subsets
// https://leetcode.com/problems/word-subsets/

object Solution {
  def wordSubsets(words1: Array[String], words2: Array[String]): List[String] = {
    val need = Array.ofDim[Int](26)
    words2.foreach { w =>
      val cnt = Array.ofDim[Int](26)
      w.foreach { c => cnt(c - 'a') += 1 }
      var i = 0
      while (i < 26) {
        need(i) = math.max(need(i), cnt(i))
        i += 1
      }
    }
    val ans = scala.collection.mutable.ListBuffer[String]()
    words1.foreach { w =>
      val cnt = Array.ofDim[Int](26)
      w.foreach { c => cnt(c - 'a') += 1 }
      var ok = true
      var i = 0
      while (i < 26) {
        if (cnt(i) < need(i)) ok = false
        i += 1
      }
      if (ok) ans += w
    }
    ans.toList
  }
}
