// LeetCode 1905 - Count Sub Islands
// https://leetcode.com/problems/count-sub-islands/

object Solution {
  def countSubIslands(grid1: Array[Array[Int]], grid2: Array[Array[Int]]): Int = {
    val rows = grid2.length
    val cols = grid2(0).length

    def dfs(r: Int, c: Int): Boolean = {
      if (r < 0 || c < 0 || r >= rows || c >= cols || grid2(r)(c) == 0) return true
      grid2(r)(c) = 0
      var ok = grid1(r)(c) == 1
      if (!dfs(r + 1, c)) ok = false
      if (!dfs(r - 1, c)) ok = false
      if (!dfs(r, c + 1)) ok = false
      if (!dfs(r, c - 1)) ok = false
      ok
    }

    var ans = 0
    for (r <- 0 until rows; c <- 0 until cols) {
      if (grid2(r)(c) == 1 && dfs(r, c)) ans += 1
    }
    ans
  }
}
