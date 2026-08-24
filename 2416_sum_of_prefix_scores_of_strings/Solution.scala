// LeetCode 2416 - Sum of Prefix Scores of Strings
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

object Solution {
  private class TrieNode {
    val child = Array.fill[TrieNode](26)(null)
    var cnt = 0
  }

  def sumPrefixScores(words: Array[String]): Array[Int] = {
    val root = new TrieNode()
    words.foreach { w =>
      var cur = root
      var i = 0
      while (i < w.length) {
        val c = w.charAt(i) - 'a'
        if (cur.child(c) == null) cur.child(c) = new TrieNode()
        cur = cur.child(c)
        cur.cnt += 1
        i += 1
      }
    }
    val ans = new Array[Int](words.length)
    var wi = 0
    while (wi < words.length) {
      var cur = root
      var sum = 0
      var i = 0
      val w = words(wi)
      while (i < w.length) {
        cur = cur.child(w.charAt(i) - 'a')
        sum += cur.cnt
        i += 1
      }
      ans(wi) = sum
      wi += 1
    }
    ans
  }
}
