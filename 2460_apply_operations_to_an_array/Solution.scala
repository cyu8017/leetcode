// LeetCode 2460 - Apply Operations to an Array
// https://leetcode.com/problems/apply-operations-to-an-array/

object Solution {
  def applyOperations(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    var i = 0
    while (i + 1 < n) {
      if (nums(i) == nums(i + 1)) {
        nums(i) *= 2
        nums(i + 1) = 0
      }
      i += 1
    }
    val ans = new Array[Int](n)
    var j = 0
    i = 0
    while (i < n) {
      if (nums(i) != 0) {
        ans(j) = nums(i)
        j += 1
      }
      i += 1
    }
    ans
  }
}
