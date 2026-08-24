// LeetCode 0611 - Valid Triangle Number
// https://leetcode.com/problems/valid-triangle-number/

object Solution {
  def triangleNumber(nums: Array[Int]): Int = {
    scala.util.Sorting.quickSort(nums)
    val n = nums.length
    var count = 0
    var k = n - 1
    while (k >= 2) {
      var left = 0
      var right = k - 1
      while (left < right) {
        if (nums(left) + nums(right) > nums(k)) {
          count += right - left
          right -= 1
        } else {
          left += 1
        }
      }
      k -= 1
    }
    count
  }
}
