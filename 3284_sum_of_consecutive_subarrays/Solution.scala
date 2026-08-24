// LeetCode 3284 - Sum of Consecutive Subarrays
// https://leetcode.com/problems/sum-of-consecutive-subarrays/

object Solution {
  def rangeSum(nums: Array[Int]): Int = {
    val mod = 1000000007
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      var j = i
      while (j + 1 < n && (nums(j + 1) == nums(j) + 1 || nums(j + 1) == nums(j) - 1)) j += 1
      var L = i
      while (L <= j) {
        var s = 0
        var R = L
        while (R <= j) {
          s += nums(R)
          ans = (ans + s) % mod
          R += 1
        }
        L += 1
      }
      i = j + 1
    }
    ans
  }
}
