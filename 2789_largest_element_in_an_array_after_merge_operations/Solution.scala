// LeetCode 2789 - Largest Element in an Array after Merge Operations
// https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

object Solution {
  def maxArrayValue(nums: Array[Int]): Long = {
    val n = nums.length
    var cur = nums(n - 1).toLong
    var ans = cur
    var i = n - 2
    while (i >= 0) {
      if (nums(i) <= cur) cur += nums(i)
      else cur = nums(i)
      ans = math.max(ans, cur)
      i -= 1
    }
    ans
  }
}
