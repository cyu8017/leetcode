// LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
// https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

object Solution {
  def isThereAPath(grid: Array[Array[Int]]): Boolean = {
    val m = grid.length
    val n = grid(0).length
    if ((m + n - 1) % 2 != 0) return false
    val target = (m + n - 1) / 2
    val memo = scala.collection.mutable.Map.empty[Long, Boolean]

    def key(r: Int, c: Int, bal: Int): Long = {
      (r.toLong << 40) | (c.toLong << 20) | (bal & 0xfffffL)
    }

    def dfs(r: Int, c: Int, bal0: Int): Boolean = {
      if (r >= m || c >= n) return false
      val bal = bal0 + grid(r)(c)
      if (bal > target || bal + (m - 1 - r) + (n - 1 - c) < target) return false
      if (r == m - 1 && c == n - 1) return bal == target
      val k = key(r, c, bal)
      memo.get(k) match {
        case Some(cached) => cached
        case None =>
          val ok = dfs(r + 1, c, bal) || dfs(r, c + 1, bal)
          memo(k) = ok
          ok
      }
    }

    dfs(0, 0, 0)
  }
}
