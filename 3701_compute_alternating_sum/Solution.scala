// LeetCode 3701 - Compute Alternating Sum
// https://leetcode.com/problems/compute-alternating-sum/

object Solution {
  def alternatingSum(nums: Array[Int]): Int = {
    var ans = 0
    var i = 0
    while (i < nums.length) {
      if (i % 2 == 0) ans += nums(i)
      else ans -= nums(i)
      i += 1
    }
    ans
  }
}
