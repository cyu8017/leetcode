// LeetCode 3552 - Grid Teleportation Traversal
// https://leetcode.com/problems/grid-teleportation-traversal/

object Solution {
  def minMoves(matrix: Array[String]): Int = {
    val m = matrix.length
    val n = matrix(0).length
    val g = scala.collection.mutable.HashMap.empty[Char, java.util.ArrayList[Array[Int]]]
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val c = matrix(i).charAt(j)
        if (Character.isLetter(c)) {
          if (!g.contains(c)) g(c) = new java.util.ArrayList[Array[Int]]()
          g(c).add(Array(i, j))
        }
        j += 1
      }
      i += 1
    }
    val dirs = Array(-1, 0, 1, 0, -1)
    val INF = 1 << 30
    val dist = Array.fill(m, n)(INF)
    dist(0)(0) = 0
    val q = new java.util.ArrayDeque[Array[Int]]()
    q.add(Array(0, 0))
    while (!q.isEmpty) {
      val cur = q.pollFirst()
      i = cur(0)
      val j = cur(1)
      val d = dist(i)(j)
      if (i == m - 1 && j == n - 1) return d
      val c = matrix(i).charAt(j)
      if (g.contains(c)) {
        val it = g(c).iterator()
        while (it.hasNext) {
          val p = it.next()
          val x = p(0); val y = p(1)
          if (d < dist(x)(y)) {
            dist(x)(y) = d
            q.addFirst(Array(x, y))
          }
        }
        g.remove(c)
      }
      var idx = 0
      while (idx < 4) {
        val x = i + dirs(idx)
        val y = j + dirs(idx + 1)
        if (0 <= x && x < m && 0 <= y && y < n && matrix(x).charAt(y) != '#' && d + 1 < dist(x)(y)) {
          dist(x)(y) = d + 1
          q.addLast(Array(x, y))
        }
        idx += 1
      }
    }
    -1
  }
}
