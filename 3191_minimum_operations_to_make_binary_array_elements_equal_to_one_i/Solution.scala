// LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    var ans = 0
    var i = 0
    while (i < nums.length) {
      if (nums(i) == 0) {
        if (i + 2 >= nums.length) return -1
        nums(i + 1) ^= 1
        nums(i + 2) ^= 1
        ans += 1
      }
      i += 1
    }
    ans
  }
}
