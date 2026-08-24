// LeetCode 2606 - Find the Substring With Maximum Cost
// https://leetcode.com/problems/find-the-substring-with-maximum-cost/

object Solution {
  def maximumCostSubstring(s: String, chars: String, vals: Array[Int]): Int = {
    val value = Array.tabulate(26)(i => i + 1)
    var i = 0
    while (i < chars.length) {
      value(chars.charAt(i) - 'a') = vals(i)
      i += 1
    }
    var best = 0
    var cur = 0
    s.foreach { c =>
      cur += value(c - 'a')
      if (cur < 0) cur = 0
      if (cur > best) best = cur
    }
    best
  }
}
