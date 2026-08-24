// LeetCode 2708 - Maximum Strength of a Group
// https://leetcode.com/problems/maximum-strength-of-a-group/

object Solution {
  def maxStrength(nums: Array[Int]): Long = {
    scala.util.Sorting.quickSort(nums)
    val n = nums.length
    if (n == 1) return nums(0).toLong
    var prod = 1L
    var used = false
    var i = 0
    while (i + 1 < n && nums(i) < 0 && nums(i + 1) < 0) {
      prod *= nums(i).toLong * nums(i + 1)
      used = true
      i += 2
    }
    val negLeft = i < n && nums(i) < 0
    while (i < n) {
      if (nums(i) > 0) {
        prod *= nums(i)
        used = true
      }
      i += 1
    }
    if (!used) {
      if (negLeft) {
        var j = 0
        while (j < n) {
          if (nums(j) == 0) return 0
          j += 1
        }
        return nums(n - 1).toLong
      }
      return 0
    }
    prod
  }
}
