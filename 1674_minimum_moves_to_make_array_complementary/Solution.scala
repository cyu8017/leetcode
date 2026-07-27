// LeetCode 1674 - Minimum Moves to Make Array Complementary
// https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

object Solution {
  def minMoves(nums: Array[Int], limit: Int): Int = {
    val n = nums.length
    val d = Array.fill(2 * limit + 2)(0)
    for (i <- 0 until n / 2) {
      val a = nums(i)
      val b = nums(n - 1 - i)
      val lo = math.min(a, b) + 1
      val hi = math.max(a, b) + limit
      val s = a + b
      d(2) += 2
      d(lo) -= 1
      d(s) -= 1
      d(s + 1) += 1
      d(hi + 1) += 1
    }
    var ans = Int.MaxValue
    var cur = 0
    for (s <- 2 to 2 * limit) {
      cur += d(s)
      if (cur < ans) ans = cur
    }
    ans
  }
}
