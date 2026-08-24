// LeetCode 0694 - Number of Distinct Islands
// https://leetcode.com/problems/number-of-distinct-islands/

object Solution {
  def numDistinctIslands(grid: Array[Array[Int]]): Int = {
    if (grid == null || grid.isEmpty) return 0
    val shapes = scala.collection.mutable.HashSet.empty[String]
    def dfs(r: Int, c: Int, br: Int, bc: Int, path: scala.collection.mutable.ArrayBuffer[String]): Unit = {
      if (r < 0 || r >= grid.length || c < 0 || c >= grid(0).length || grid(r)(c) == 0) return
      grid(r)(c) = 0
      path += s"${r - br},${c - bc}"
      dfs(r + 1, c, br, bc, path)
      dfs(r - 1, c, br, bc, path)
      dfs(r, c + 1, br, bc, path)
      dfs(r, c - 1, br, bc, path)
    }
    var i = 0
    while (i < grid.length) {
      var j = 0
      while (j < grid(0).length) {
        if (grid(i)(j) == 1) {
          val path = scala.collection.mutable.ArrayBuffer.empty[String]
          dfs(i, j, i, j, path)
          shapes += path.mkString(";")
        }
        j += 1
      }
      i += 1
    }
    shapes.size
  }
}
