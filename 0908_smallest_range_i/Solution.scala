// LeetCode 0908 - Smallest Range I
// https://leetcode.com/problems/smallest-range-i/

object Solution {
  def smallestRangeI(nums: Array[Int], k: Int): Int = {
    var mn = nums(0)
    var mx = nums(0)
    nums.foreach { x =>
      mn = math.min(mn, x)
      mx = math.max(mx, x)
    }
    math.max(0, mx - mn - 2 * k)
  }
}
