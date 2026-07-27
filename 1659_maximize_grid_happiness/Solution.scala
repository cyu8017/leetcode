// LeetCode 1659 - Maximize Grid Happiness
// https://leetcode.com/problems/maximize-grid-happiness/

object Solution {
  def getMaxGridHappiness(m: Int, n: Int, introvertsCount: Int, extrovertsCount: Int): Int = {
    var states = 1
    for (_ <- 0 until n) states *= 3
    val cells = Array.ofDim[Int](states, n)
    val intro = Array.fill(states)(0)
    val extro = Array.fill(states)(0)
    val row = Array.fill(states)(0)
    for (s <- 0 until states) {
      var x = s
      for (j <- 0 until n) {
        cells(s)(j) = x % 3
        x /= 3
      }
      var value = 0
      for (j <- 0 until n) {
        val z = cells(s)(j)
        if (z == 1) { intro(s) += 1; value += 120 }
        else if (z == 2) { extro(s) += 1; value += 40 }
      }
      for (j <- 1 until n) value += pairCost(cells(s)(j - 1), cells(s)(j))
      row(s) = value
    }
    val compat = Array.ofDim[Int](states, states)
    for (a <- 0 until states; b <- 0 until states) {
      var v = 0
      for (j <- 0 until n) v += pairCost(cells(a)(j), cells(b)(j))
      compat(a)(b) = v
    }
    val memo = scala.collection.mutable.Map.empty[(Int, Int, Int, Int), Int]
    def dfs(r: Int, prev: Int, i: Int, e: Int): Int = {
      if (r == m) return 0
      val key = (r, prev, i, e)
      if (memo.contains(key)) return memo(key)
      var best = 0
      for (s <- 0 until states if intro(s) <= i && extro(s) <= e) {
        val value = row(s) + compat(prev)(s) + dfs(r + 1, s, i - intro(s), e - extro(s))
        if (value > best) best = value
      }
      memo(key) = best
      best
    }
    dfs(0, 0, introvertsCount, extrovertsCount)
  }

  private def pairCost(a: Int, b: Int): Int = {
    if (a == 0 || b == 0) 0
    else {
      val va = if (a == 1) -30 else 20
      val vb = if (b == 1) -30 else 20
      va + vb
    }
  }
}
