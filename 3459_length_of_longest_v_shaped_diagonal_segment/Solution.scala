// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

object Solution {
  private var m = 0
  private var n = 0
  private var grid: Array[Array[Int]] = _
  private val dirs = Array(Array(1, 1), Array(1, -1), Array(-1, -1), Array(-1, 1))
  private val nextDir = Array(1, 2, 3, 0)
  private val memo = new java.util.HashMap[java.lang.Long, Integer]()

  def lenOfVDiagonal(grid0: Array[Array[Int]]): Int = {
    grid = grid0
    m = grid.length
    n = grid(0).length
    memo.clear()
    var ans = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 1) {
          var d = 0
          while (d < 4) {
            val ni = i + dirs(d)(0)
            val nj = j + dirs(d)(1)
            val best = 1 + dfs(ni, nj, d, 0, 2)
            if (best > ans) ans = best
            d += 1
          }
          if (ans < 1) ans = 1
        }
        j += 1
      }
      i += 1
    }
    ans
  }

  private def key(i: Int, j: Int, d: Int, turned: Int, expect: Int): Long =
    ((((i.toLong * 101L + j) * 5L + d) * 3L + turned) * 5L + expect)

  private def dfs(i: Int, j: Int, d: Int, turned: Int, expect: Int): Int = {
    if (i < 0 || j < 0 || i >= m || j >= n || grid(i)(j) != expect) return 0
    val k = key(i, j, d, turned, expect)
    val cached = memo.get(k)
    if (cached != null) return cached
    val ni = i + dirs(d)(0)
    val nj = j + dirs(d)(1)
    val nx = if (expect == 2) 0 else 2
    var best = 1 + dfs(ni, nj, d, turned, nx)
    if (turned == 0) {
      val nd = nextDir(d)
      val ti = i + dirs(nd)(0)
      val tj = j + dirs(nd)(1)
      val cand = 1 + dfs(ti, tj, nd, 1, nx)
      if (cand > best) best = cand
    }
    memo.put(k, best)
    best
  }
}
