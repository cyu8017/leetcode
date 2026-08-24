// LeetCode 2909 - Minimum Sum of Mountain Triplets II
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

object Solution {
  def minimumSum(nums: Array[Int]): Int = {
    val n = nums.length
    val left = Array.fill(n)(0)
    val right = Array.fill(n)(0)
    var mn = 1 << 30
    for (i <- 0 until n) {
      left(i) = mn
      if (nums(i) < mn) mn = nums(i)
    }
    mn = 1 << 30
    for (i <- n - 1 to 0 by -1) {
      right(i) = mn
      if (nums(i) < mn) mn = nums(i)
    }
    var ans = 1 << 30
    for (j <- 1 until n - 1) {
      if (left(j) < nums(j) && right(j) < nums(j)) {
        val cand = left(j) + nums(j) + right(j)
        if (cand < ans) ans = cand
      }
    }
    if (ans == (1 << 30)) -1 else ans
  }
}
