// LeetCode 0910 - Smallest Range II
// https://leetcode.com/problems/smallest-range-ii/

object Solution {
  def smallestRangeII(nums: Array[Int], k: Int): Int = {
    val arr = nums.sorted
    var ans = arr.last - arr(0)
    var i = 0
    while (i + 1 < arr.length) {
      val lo = math.min(arr(0) + k, arr(i + 1) - k)
      val hi = math.max(arr.last - k, arr(i) + k)
      ans = math.min(ans, hi - lo)
      i += 1
    }
    ans
  }
}
