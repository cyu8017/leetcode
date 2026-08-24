// LeetCode 3277 - Maximum XOR Score Subarray Queries
// https://leetcode.com/problems/maximum-xor-score-subarray-queries/

object Solution {
  def maximumSubarrayXor(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = nums.length
    val f = Array.ofDim[Int](n, n)
    var i = 0
    while (i < n) { f(i)(i) = nums(i); i += 1 }
    var length = 2
    while (length <= n) {
      i = 0
      while (i + length - 1 < n) {
        val j = i + length - 1
        f(i)(j) = f(i)(j - 1) ^ f(i + 1)(j)
        i += 1
      }
      length += 1
    }
    val best = Array.ofDim[Int](n, n)
    i = 0
    while (i < n) { best(i)(i) = f(i)(i); i += 1 }
    length = 2
    while (length <= n) {
      i = 0
      while (i + length - 1 < n) {
        val j = i + length - 1
        best(i)(j) = math.max(f(i)(j), math.max(best(i)(j - 1), best(i + 1)(j)))
        i += 1
      }
      length += 1
    }
    val ans = new Array[Int](queries.length)
    i = 0
    while (i < queries.length) {
      ans(i) = best(queries(i)(0))(queries(i)(1))
      i += 1
    }
    ans
  }
}
