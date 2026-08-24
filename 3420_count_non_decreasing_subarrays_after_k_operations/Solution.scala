// LeetCode 3420 - Count Non-Decreasing Subarrays After K Operations
// https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

object Solution {
  def countNonDecreasingSubarrays(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    var ans = 0L
    var i = 0
    while (i < n) {
      var cost = 0L
      var maxV = nums(i)
      var j = i
      var stop = false
      while (j < n && !stop) {
        if (nums(j) >= maxV) maxV = nums(j)
        else cost += maxV - nums(j)
        if (cost > k) stop = true
        else ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
