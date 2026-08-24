// LeetCode 0741 - Cherry Pickup
// https://leetcode.com/problems/cherry-pickup/

object Solution {
  def cherryPickup(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val memo = Array.fill(n, n, n)(Int.MinValue)
    def dp(r1: Int, c1: Int, c2: Int): Int = {
      val r2 = r1 + c1 - c2
      if (r1 >= n || c1 >= n || r2 >= n || c2 >= n || grid(r1)(c1) == -1 || grid(r2)(c2) == -1) return -1000000000
      if (r1 == n - 1 && c1 == n - 1) return grid(r1)(c1)
      if (memo(r1)(c1)(c2) != Int.MinValue) return memo(r1)(c1)(c2)
      var cherries = grid(r1)(c1)
      if (r1 != r2 || c1 != c2) cherries += grid(r2)(c2)
      cherries += math.max(
        math.max(dp(r1 + 1, c1, c2), dp(r1, c1 + 1, c2)),
        math.max(dp(r1 + 1, c1, c2 + 1), dp(r1, c1 + 1, c2 + 1))
      )
      memo(r1)(c1)(c2) = cherries
      cherries
    }
    math.max(0, dp(0, 0, 0))
  }
}
