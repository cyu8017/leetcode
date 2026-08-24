// LeetCode 0711 - Number of Distinct Islands II
// https://leetcode.com/problems/number-of-distinct-islands-ii/

object Solution {
  def numDistinctIslands2(grid: Array[Array[Int]]): Int = {
    if (grid == null || grid.isEmpty) return 0
    val m = grid.length
    val n = grid(0).length
    val shapes = scala.collection.mutable.HashSet.empty[String]
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 1) {
          val cells = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
          dfs(grid, i, j, m, n, cells)
          shapes += canonical(cells)
        }
        j += 1
      }
      i += 1
    }
    shapes.size
  }

  private def dfs(grid: Array[Array[Int]], r: Int, c: Int, m: Int, n: Int, cells: scala.collection.mutable.ArrayBuffer[Array[Int]]): Unit = {
    if (r < 0 || r >= m || c < 0 || c >= n || grid(r)(c) == 0) return
    grid(r)(c) = 0
    cells += Array(r, c)
    dfs(grid, r + 1, c, m, n, cells)
    dfs(grid, r - 1, c, m, n, cells)
    dfs(grid, r, c + 1, m, n, cells)
    dfs(grid, r, c - 1, m, n, cells)
  }

  private def canonical(cells: scala.collection.mutable.ArrayBuffer[Array[Int]]): String = {
    val signs = Array(
      Array(1, 1, 0), Array(1, -1, 0), Array(-1, 1, 0), Array(-1, -1, 0),
      Array(1, 1, 1), Array(1, -1, 1), Array(-1, 1, 1), Array(-1, -1, 1)
    )
    var best: String = null
    for (s <- signs) {
      val pts = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
      for (p <- cells) {
        val x = p(0)
        val y = p(1)
        val nx = if (s(2) == 0) s(0) * x else s(0) * y
        val ny = if (s(2) == 0) s(1) * y else s(1) * x
        pts += Array(nx, ny)
      }
      var minX = Int.MaxValue
      var minY = Int.MaxValue
      for (p <- pts) {
        minX = math.min(minX, p(0))
        minY = math.min(minY, p(1))
      }
      for (p <- pts) {
        p(0) -= minX
        p(1) -= minY
      }
      val sorted = pts.sortWith((a, b) => if (a(0) != b(0)) a(0) < b(0) else a(1) < b(1))
      val key = sorted.map(p => s"${p(0)},${p(1)}").mkString(";")
      if (best == null || key < best) best = key
    }
    best
  }
}
