// LeetCode 2014 - Longest Subsequence Repeated K Times
// https://leetcode.com/problems/longest-subsequence-repeated-k-times/

object Solution {
  def longestSubsequenceRepeatedK(s: String, k: Int): String = {
    val freq = Array.ofDim[Int](26)
    s.foreach { c => freq(c - 'a') += 1 }
    val chars = new StringBuilder
    var c = 25
    while (c >= 0) {
      if (freq(c) >= k) chars.append(('a' + c).toChar)
      c -= 1
    }
    def isSubseq(t: String): Boolean = {
      var need = 0
      var times = 0
      var i = 0
      while (i < s.length) {
        if (s.charAt(i) == t.charAt(need)) {
          need += 1
          if (need == t.length) {
            times += 1
            if (times == k) return true
            need = 0
          }
        }
        i += 1
      }
      false
    }
    var best = ""
    val q = scala.collection.mutable.Queue("")
    while (q.nonEmpty) {
      val cur = q.dequeue()
      var i = 0
      while (i < chars.length) {
        val nxt = cur + chars.charAt(i)
        if (isSubseq(nxt)) {
          if (nxt.length > best.length || (nxt.length == best.length && nxt > best)) best = nxt
          q.enqueue(nxt)
        }
        i += 1
      }
    }
    best
  }
}
