// LeetCode 2104 - Sum of Subarray Ranges
// https://leetcode.com/problems/sum-of-subarray-ranges/

object Solution {
  def subArrayRanges(nums: Array[Int]): Long = {
    val n = nums.length
    var ans = 0L
    var i = 0
    while (i < n) {
      var mn = nums(i)
      var mx = nums(i)
      var j = i
      while (j < n) {
        mn = math.min(mn, nums(j))
        mx = math.max(mx, nums(j))
        ans += mx - mn
        j += 1
      }
      i += 1
    }
    ans
  }
}
