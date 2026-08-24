// LeetCode 2535 - Difference Between Element Sum and Digit Sum of an Array
// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

object Solution {
  def differenceOfSum(nums: Array[Int]): Int = {
    var elem = 0
    var digit = 0
    nums.foreach { num =>
      elem += num
      var x = num
      while (x > 0) {
        digit += x % 10
        x /= 10
      }
    }
    math.abs(elem - digit)
  }
}
