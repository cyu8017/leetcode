// LeetCode 3364 - Minimum Positive Sum Subarray
// https://leetcode.com/problems/minimum-positive-sum-subarray/

object Solution {
  def minimumSumSubarray(nums: Array[Int], l: Int, r: Int): Int = {
    val n = nums.length
    val pref = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + nums(i)
      i += 1
    }
    var ans = Int.MaxValue
    var found = false
    i = 0
    while (i < n) {
      var length = l
      while (length <= r && i + length <= n) {
        val s = pref(i + length) - pref(i)
        if (s > 0 && s < ans) {
          ans = s
          found = true
        }
        length += 1
      }
      i += 1
    }
    if (found) ans else -1
  }
}
