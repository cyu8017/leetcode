// LeetCode 0724 - Find Pivot Index
// https://leetcode.com/problems/find-pivot-index/

object Solution {
  def pivotIndex(nums: Array[Int]): Int = {
    var total = 0
    for (x <- nums) total += x
    var left = 0
    var i = 0
    while (i < nums.length) {
      if (left == total - left - nums(i)) return i
      left += nums(i)
      i += 1
    }
    -1
  }
}
