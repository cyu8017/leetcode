// LeetCode 3040 - Maximum Number of Operations With the Same Score II
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

object Solution {
  def maxOperations(nums: Array[Int]): Int = {
    val n = nums.length
    var f: Array[Array[Int]] = null
    var s = 0
    def dfs(i: Int, j: Int): Int = {
      if (j - i < 1) return 0
      if (f(i)(j) != -1) return f(i)(j)
      var ans = 0
      if (nums(i) + nums(i + 1) == s) ans = math.max(ans, 1 + dfs(i + 2, j))
      if (nums(i) + nums(j) == s) ans = math.max(ans, 1 + dfs(i + 1, j - 1))
      if (nums(j - 1) + nums(j) == s) ans = math.max(ans, 1 + dfs(i, j - 2))
      f(i)(j) = ans
      ans
    }
    def g(i0: Int, j0: Int, score: Int): Int = {
      f = Array.fill(n, n)(-1)
      s = score
      dfs(i0, j0)
    }
    val a = g(2, n - 1, nums(0) + nums(1))
    val b = g(0, n - 3, nums(n - 1) + nums(n - 2))
    val c = g(1, n - 2, nums(0) + nums(n - 1))
    1 + math.max(a, math.max(b, c))
  }
}
