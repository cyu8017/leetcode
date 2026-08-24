// LeetCode 2389 - Longest Subsequence With Limited Sum
// https://leetcode.com/problems/longest-subsequence-with-limited-sum/

object Solution {
  def answerQueries(nums: Array[Int], queries: Array[Int]): Array[Int] = {
    java.util.Arrays.sort(nums)
    var i = 1
    while (i < nums.length) {
      nums(i) += nums(i - 1)
      i += 1
    }
    val ans = Array.fill(queries.length)(0)
    i = 0
    while (i < queries.length) {
      var lo = 0
      var hi = nums.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (nums(mid) <= queries(i)) lo = mid + 1
        else hi = mid
      }
      ans(i) = lo
      i += 1
    }
    ans
  }
}
