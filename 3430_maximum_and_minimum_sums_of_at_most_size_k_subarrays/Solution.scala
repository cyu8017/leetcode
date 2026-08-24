// LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

object Solution {
  def minMaxSubarraySum(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    var ans = 0L
    var i = 0
    while (i < n) {
      var mn = nums(i)
      var mx = nums(i)
      var j = i
      while (j < n && j - i + 1 <= k) {
        if (nums(j) < mn) mn = nums(j)
        if (nums(j) > mx) mx = nums(j)
        ans += mn + mx
        j += 1
      }
      i += 1
    }
    ans
  }
}
