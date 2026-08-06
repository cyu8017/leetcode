// LeetCode 1589 - Maximum Sum Obtained of Any Permutation
// https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

object Solution {
  def maxSumRangeQuery(nums: Array[Int], requests: Array[Array[Int]]): Int = {
    val MOD = 1000000007L
    val diff = Array.fill(nums.length + 1)(0)
    for (Array(left, right) <- requests) {
      diff(left) += 1
      diff(right + 1) -= 1
    }
    for (i <- 1 until nums.length) diff(i) += diff(i - 1)
    val a = nums.sorted
    val b = diff.take(nums.length).sorted
    (a.zip(b).map { case (x, y) => x.toLong * y }.sum % MOD).toInt
  }
}
