// LeetCode 3565 - Sequential Grid Path Cover
// https://leetcode.com/problems/sequential-grid-path-cover/

object Solution {
  def findPath(grid: Array[Array[Int]], k: Int): java.util.List[java.util.List[Integer]] = {
    val m = grid.length
    val n = grid(0).length
    var st = 0L
    val path = new java.util.ArrayList[java.util.List[Integer]]()
    val dirs = Array(-1, 0, 1, 0, -1)

    def f(i: Int, j: Int): Int = i * n + j

    def dfs(i: Int, j: Int, v0: Int): Boolean = {
      var v = v0
      val cell = new java.util.ArrayList[Integer]()
      cell.add(i); cell.add(j)
      path.add(cell)
      if (path.size() == m * n) return true
      val idx = f(i, j)
      st |= 1L << idx
      if (grid(i)(j) == v) v += 1
      var t = 0
      while (t < 4) {
        val x = i + dirs(t)
        val y = j + dirs(t + 1)
        if (0 <= x && x < m && 0 <= y && y < n) {
          val idx2 = f(x, y)
          if (((st >> idx2) & 1L) == 0 && (grid(x)(y) == 0 || grid(x)(y) == v)) {
            if (dfs(x, y, v)) return true
          }
        }
        t += 1
      }
      path.remove(path.size() - 1)
      st ^= 1L << idx
      false
    }

    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 0 || grid(i)(j) == 1) {
          if (dfs(i, j, 1)) return path
          path.clear()
          st = 0
        }
        j += 1
      }
      i += 1
    }
    new java.util.ArrayList[java.util.List[Integer]]()
  }
}
