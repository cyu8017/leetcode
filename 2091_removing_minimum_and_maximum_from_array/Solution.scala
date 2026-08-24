// LeetCode 2091 - Removing Minimum and Maximum From Array
// https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

object Solution {
  def minimumDeletions(nums: Array[Int]): Int = {
    val n = nums.length
    var mi = 0
    var ma = 0
    var i = 0
    while (i < n) {
      if (nums(i) < nums(mi)) mi = i
      if (nums(i) > nums(ma)) ma = i
      i += 1
    }
    val lo = math.min(mi, ma)
    val hi = math.max(mi, ma)
    math.min(hi + 1, math.min(n - lo, lo + 1 + n - hi))
  }
}
