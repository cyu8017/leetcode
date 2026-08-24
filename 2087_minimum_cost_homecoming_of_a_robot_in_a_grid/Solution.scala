// LeetCode 2087 - Minimum Cost Homecoming of a Robot in a Grid
// https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

object Solution {
  def minCost(startPos: Array[Int], homePos: Array[Int], rowCosts: Array[Int], colCosts: Array[Int]): Int = {
    var ans = 0
    val sr = startPos(0)
    val sc = startPos(1)
    val hr = homePos(0)
    val hc = homePos(1)
    if (sr < hr) {
      var r = sr + 1
      while (r <= hr) { ans += rowCosts(r); r += 1 }
    } else {
      var r = sr - 1
      while (r >= hr) { ans += rowCosts(r); r -= 1 }
    }
    if (sc < hc) {
      var c = sc + 1
      while (c <= hc) { ans += colCosts(c); c += 1 }
    } else {
      var c = sc - 1
      while (c >= hc) { ans += colCosts(c); c -= 1 }
    }
    ans
  }
}
