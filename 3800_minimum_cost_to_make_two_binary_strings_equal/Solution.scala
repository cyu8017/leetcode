// LeetCode 3800 - Minimum Cost To Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

object Solution {
  def minimumCost(s: String, t: String, flipCost: Int, swapCost: Int, crossCost: Int): Long = {
    val diff = Array(0L, 0L)
    val n = s.length
    var i = 0
    while (i < n) {
      if (s.charAt(i) != t.charAt(i)) diff(s.charAt(i) - '0') += 1
      i += 1
    }
    var ans = (diff(0) + diff(1)) * flipCost
    val mx = math.max(diff(0), diff(1))
    val mn = math.min(diff(0), diff(1))
    ans = math.min(ans, mn * swapCost + (mx - mn) * flipCost)
    val avg = (mx + mn) / 2
    ans = math.min(ans, (avg - mn) * crossCost + avg * swapCost + (mx + mn - avg * 2) * flipCost)
    ans
  }
}
