// LeetCode 2444 - Count Subarrays With Fixed Bounds
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

object Solution {
  def countSubarrays(nums: Array[Int], minK: Int, maxK: Int): Long = {
    var ans = 0L
    var imin = -1
    var imax = -1
    var ibad = -1
    var i = 0
    while (i < nums.length) {
      val x = nums(i)
      if (x < minK || x > maxK) ibad = i
      if (x == minK) imin = i
      if (x == maxK) imax = i
      val bound = if (imin < imax) imin else imax
      if (bound > ibad) ans += bound - ibad
      i += 1
    }
    ans
  }
}
