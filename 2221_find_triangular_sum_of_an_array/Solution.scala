// LeetCode 2221 - Find Triangular Sum of an Array
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

object Solution {
  def triangularSum(nums: Array[Int]): Int = {
    var cur = nums
    while (cur.length > 1) {
      val next = new Array[Int](cur.length - 1)
      var i = 0
      while (i < next.length) {
        next(i) = (cur(i) + cur(i + 1)) % 10
        i += 1
      }
      cur = next
    }
    cur(0)
  }
}
