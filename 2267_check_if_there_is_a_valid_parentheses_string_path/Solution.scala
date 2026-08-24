// LeetCode 2267 - Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

object Solution {
  def hasValidPath(grid: Array[Array[Char]]): Boolean = {
    val m = grid.length
    val n = grid(0).length
    if ((m + n - 1) % 2 == 1 || grid(0)(0) == ')' || grid(m - 1)(n - 1) == '(') return false
    val vis = scala.collection.mutable.HashSet.empty[Long]
    def dfs(r: Int, c: Int, bal0: Int): Boolean = {
      if (r >= m || c >= n) return false
      val bal = bal0 + (if (grid(r)(c) == '(') 1 else -1)
      if (bal < 0) return false
      if (r == m - 1 && c == n - 1) return bal == 0
      val k = (((r.toLong * n + c) << 10) | bal)
      if (!vis.add(k)) return false
      dfs(r + 1, c, bal) || dfs(r, c + 1, bal)
    }
    dfs(0, 0, 0)
  }
}
