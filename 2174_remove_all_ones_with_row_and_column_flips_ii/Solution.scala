// LeetCode 2174 - Remove All Ones With Row and Column Flips II
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

object Solution {
  def removeOnes(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val ones = scala.collection.mutable.ArrayBuffer.empty[(Int, Int)]
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 1) ones += ((i, j))
        j += 1
      }
      i += 1
    }
    if (ones.isEmpty) return 0
    var ans = m + n
    def dfs(idx0: Int, flips: Int): Unit = {
      if (flips >= ans) return
      var idx = idx0
      while (idx < ones.length && grid(ones(idx)._1)(ones(idx)._2) == 0) idx += 1
      if (idx == ones.length) { ans = flips; return }
      val (r, c) = ones(idx)
      val changed = scala.collection.mutable.ArrayBuffer.empty[(Int, Int)]
      var j = 0
      while (j < n) {
        if (grid(r)(j) == 1) { grid(r)(j) = 0; changed += ((r, j)) }
        j += 1
      }
      dfs(idx + 1, flips + 1)
      changed.foreach { case (x, y) => grid(x)(y) = 1 }
      changed.clear()
      i = 0
      while (i < m) {
        if (grid(i)(c) == 1) { grid(i)(c) = 0; changed += ((i, c)) }
        i += 1
      }
      dfs(idx + 1, flips + 1)
      changed.foreach { case (x, y) => grid(x)(y) = 1 }
    }
    dfs(0, 0)
    ans
  }
}
