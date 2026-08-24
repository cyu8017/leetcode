// LeetCode 3130 - Find All Possible Stable Binary Arrays II
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

object Solution {
  private val MOD = 1000000007

  def numberOfStableArrays(zero: Int, one: Int, limit: Int): Int = {
    val f = Array.fill(zero + 1, one + 1, 2)(-1)

    def dfs(i: Int, j: Int, k: Int): Int = {
      if (i < 0 || j < 0) return 0
      if (i == 0) return if (k == 1 && j <= limit) 1 else 0
      if (j == 0) return if (k == 0 && i <= limit) 1 else 0
      if (f(i)(j)(k) != -1) return f(i)(j)(k)
      val res =
        if (k == 0) (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - dfs(i - limit - 1, j, 1) + MOD) % MOD
        else (dfs(i, j - 1, 0) + dfs(i, j - 1, 1) - dfs(i, j - limit - 1, 0) + MOD) % MOD
      f(i)(j)(k) = res
      res
    }

    (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD
  }
}
