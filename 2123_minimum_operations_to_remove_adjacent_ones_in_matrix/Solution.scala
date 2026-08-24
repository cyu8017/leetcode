// LeetCode 2123 - Minimum Operations to Remove Adjacent Ones in Matrix
// https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/

object Solution {
  def minimumOperations(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val id = Array.fill(m, n)(-1)
    var cnt = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 1) {
          id(i)(j) = cnt
          cnt += 1
        }
        j += 1
      }
      i += 1
    }
    val g = Array.fill(cnt)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val dirs = Array((0, 1), (1, 0), (0, -1), (-1, 0))
    i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 1 && (i + j) % 2 == 0) {
          val u = id(i)(j)
          dirs.foreach { case (di, dj) =>
            val ni = i + di
            val nj = j + dj
            if (ni >= 0 && nj >= 0 && ni < m && nj < n && grid(ni)(nj) == 1)
              g(u) += id(ni)(nj)
          }
        }
        j += 1
      }
      i += 1
    }
    val matchTo = Array.fill(cnt)(-1)
    def dfs(u: Int, seen: Array[Boolean]): Boolean = {
      g(u).foreach { v =>
        if (!seen(v)) {
          seen(v) = true
          if (matchTo(v) == -1 || dfs(matchTo(v), seen)) {
            matchTo(v) = u
            return true
          }
        }
      }
      false
    }
    var ans = 0
    var u = 0
    while (u < cnt) {
      var ok = false
      i = 0
      while (i < m && !ok) {
        var j = 0
        while (j < n) {
          if (id(i)(j) == u && (i + j) % 2 == 0) { ok = true }
          j += 1
        }
        i += 1
      }
      if (ok) {
        val seen = Array.fill(cnt)(false)
        if (dfs(u, seen)) ans += 1
      }
      u += 1
    }
    ans
  }
}
