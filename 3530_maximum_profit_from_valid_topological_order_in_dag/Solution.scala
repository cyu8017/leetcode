// LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
// https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

object Solution {
  def pop(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x != 0) { c += x & 1; x >>= 1 }
    c
  }

  def maxProfit(n: Int, edges: Array[Array[Int]], score: Array[Int]): Int = {
    val need = new Array[Int](n)
    val dp = Array.fill(1 << n)(-1)
    dp(0) = 0
    for (e <- edges) need(e(1)) |= 1 << e(0)
    var mask = 0
    while (mask < (1 << n)) {
      if (dp(mask) >= 0) {
        val pos = pop(mask) + 1
        var i = 0
        while (i < n) {
          if (((mask >> i) & 1) == 0 && (mask & need(i)) == need(i)) {
            val nm = mask | (1 << i)
            val v = dp(mask) + score(i) * pos
            if (v > dp(nm)) dp(nm) = v
          }
          i += 1
        }
      }
      mask += 1
    }
    dp((1 << n) - 1)
  }
}
