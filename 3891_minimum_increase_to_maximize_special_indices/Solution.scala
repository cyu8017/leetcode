// LeetCode 3891 - Minimum Increase To Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

object Solution {
  private var nums: Array[Int] = _
  private var f: Array[Array[Long]] = _
  private var n: Int = _

  def minIncrease(nums: Array[Int]): Long = {
    this.nums = nums
    n = nums.length
    f = Array.fill(n, 2)(-1L)
    dfs(1, (n & 1) ^ 1)
  }

  private def dfs(i: Int, j: Int): Long = {
    if (i >= n - 1) return 0
    if (f(i)(j) != -1) return f(i)(j)
    val cost = math.max(0, math.max(nums(i - 1), nums(i + 1)) + 1 - nums(i))
    var ans = cost.toLong + dfs(i + 2, j)
    if (j > 0) ans = math.min(ans, dfs(i + 1, 0))
    f(i)(j) = ans
    ans
  }
}
