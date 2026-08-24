// LeetCode 3613 - Minimize Maximum Component Cost
// https://leetcode.com/problems/minimize-maximum-component-cost/

object Solution {
  def minCost(n: Int, edges: Array[Array[Int]], k: Int): Int = {
    val p = Array.tabulate(n)(i => i)
    def find(x: Int): Int = {
      if (p(x) == x) x
      else {
        p(x) = find(p(x))
        p(x)
      }
    }
    if (k == n) return 0
    val sorted = edges.sortBy(_(2))
    var cnt = n
    for (e <- sorted) {
      val pu = find(e(0))
      val pv = find(e(1))
      if (pu != pv) {
        p(pu) = pv
        cnt -= 1
        if (cnt <= k) return e(2)
      }
    }
    0
  }
}
