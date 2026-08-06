// LeetCode 1914 - Cyclically Rotating a Grid
// https://leetcode.com/problems/cyclically-rotating-a-grid/

object Solution {
  def rotateGrid(grid: Array[Array[Int]], k: Int): Array[Array[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val layers = math.min(m, n) / 2
    for (layer <- 0 until layers) {
      val vals = scala.collection.mutable.ArrayBuffer.empty[Int]
      for (c <- layer until n - layer) vals += grid(layer)(c)
      for (r <- layer + 1 until m - layer) vals += grid(r)(n - layer - 1)
      if (m - 2 * layer > 1) {
        var c = n - layer - 2
        while (c >= layer) { vals += grid(m - layer - 1)(c); c -= 1 }
      }
      if (n - 2 * layer > 1) {
        var r = m - layer - 2
        while (r > layer) { vals += grid(r)(layer); r -= 1 }
      }
      val shift = k % vals.length
      val rotated = vals.drop(shift) ++ vals.take(shift)
      var idx = 0
      for (c <- layer until n - layer) { grid(layer)(c) = rotated(idx); idx += 1 }
      for (r <- layer + 1 until m - layer) { grid(r)(n - layer - 1) = rotated(idx); idx += 1 }
      if (m - 2 * layer > 1) {
        var c = n - layer - 2
        while (c >= layer) { grid(m - layer - 1)(c) = rotated(idx); idx += 1; c -= 1 }
      }
      if (n - 2 * layer > 1) {
        var r = m - layer - 2
        while (r > layer) { grid(r)(layer) = rotated(idx); idx += 1; r -= 1 }
      }
    }
    grid
  }
}
