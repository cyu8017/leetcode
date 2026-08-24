// LeetCode 3018 - Maximum Number of Removal Queries That Can Be Processed I
// https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

object Solution {
  def maximumProcessableQueries(nums: Array[Int], queries: Array[Int]): Int = {
    val n = nums.length
    val f = Array.ofDim[Int](n, n)
    val m = queries.length
    var i = 0
    while (i < n) {
      var j = n - 1
      while (j >= i) {
        if (i > 0) {
          val t = if (f(i - 1)(j) < m && nums(i - 1) >= queries(f(i - 1)(j))) 1 else 0
          f(i)(j) = math.max(f(i)(j), f(i - 1)(j) + t)
        }
        if (j + 1 < n) {
          val t = if (f(i)(j + 1) < m && nums(j + 1) >= queries(f(i)(j + 1))) 1 else 0
          f(i)(j) = math.max(f(i)(j), f(i)(j + 1) + t)
        }
        if (f(i)(j) == m) return m
        j -= 1
      }
      i += 1
    }
    var ans = 0
    i = 0
    while (i < n) {
      val t = if (f(i)(i) < m && nums(i) >= queries(f(i)(i))) 1 else 0
      ans = math.max(ans, f(i)(i) + t)
      i += 1
    }
    ans
  }
}
