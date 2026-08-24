// LeetCode 3888 - Minimum Operations To Make All Grid Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

object Solution {
  private var grid: Array[Array[Int]] = _
  private var k: Int = _
  private var m: Int = _
  private var n: Int = _

  def minOperations(grid: Array[Array[Int]], k: Int): Long = {
    this.grid = grid
    this.k = k
    m = grid.length
    n = grid(0).length
    var maxVal = grid(0)(0)
    grid.foreach { row => row.foreach { x => maxVal = math.max(maxVal, x) } }
    var t = maxVal
    while (t <= maxVal + 1) {
      val res = check(t)
      if (res != -1) return res
      t += 1
    }
    -1L
  }

  private def check(target: Int): Long = {
    val diff = Array.ofDim[Long](m + 2, n + 2)
    var totalOps = 0L
    var i = 1
    while (i <= m) {
      var j = 1
      while (j <= n) {
        diff(i)(j) += diff(i - 1)(j) + diff(i)(j - 1) - diff(i - 1)(j - 1)
        val curVal = grid(i - 1)(j - 1).toLong + diff(i)(j)
        if (curVal > target) return -1
        if (curVal < target) {
          if (i + k - 1 > m || j + k - 1 > n) return -1
          val needed = target - curVal
          totalOps += needed
          diff(i)(j) += needed
          diff(i + k)(j) -= needed
          diff(i)(j + k) -= needed
          diff(i + k)(j + k) += needed
        }
        j += 1
      }
      i += 1
    }
    totalOps
  }
}
