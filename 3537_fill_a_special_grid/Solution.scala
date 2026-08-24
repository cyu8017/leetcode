// LeetCode 3537 - Fill a Special Grid
// https://leetcode.com/problems/fill-a-special-grid/

object Solution {
  def specialGrid(n: Int): Array[Array[Int]] = {
    val m = 1 << n
    val ans = Array.ofDim[Int](m, m)
    var value = 0
    def dfs(x: Int, y: Int, k: Int): Unit = {
      if (k == 1) {
        ans(x)(y) = value
        value += 1
        return
      }
      val h = k / 2
      dfs(x, y, h)
      dfs(x + h, y, h)
      dfs(x + h, y - h, h)
      dfs(x, y - h, h)
    }
    dfs(0, m - 1, m)
    ans
  }
}
