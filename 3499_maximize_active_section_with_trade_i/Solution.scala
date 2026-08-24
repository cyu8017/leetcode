// LeetCode 3499 - Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/

object Solution {
  def maxActiveSectionsAfterTrade(s: String): Int = {
    var ones = 0
    s.foreach { c => if (c == '1') ones += 1 }
    val zeros = new java.util.ArrayList[Array[Int]]()
    val n = s.length
    var i = 0
    while (i < n) {
      if (s.charAt(i) != '0') i += 1
      else {
        var j = i
        while (j < n && s.charAt(j) == '0') j += 1
        zeros.add(Array(i, j - 1))
        i = j
      }
    }
    var best = 0
    i = 0
    while (i + 1 < zeros.size()) {
      val gain = (zeros.get(i)(1) - zeros.get(i)(0) + 1) + (zeros.get(i + 1)(1) - zeros.get(i + 1)(0) + 1)
      if (gain > best) best = gain
      i += 1
    }
    ones + best
  }
}
