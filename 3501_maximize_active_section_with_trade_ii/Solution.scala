// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

object Solution {
  def maxActiveSectionsAfterTrade(s: String, queries: Array[Array[Int]]): Array[Int] = {
    var ones = 0
    s.foreach { c => if (c == '1') ones += 1 }
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < ans.length) { ans(i) = ones; i += 1 }
    ans
  }
}
