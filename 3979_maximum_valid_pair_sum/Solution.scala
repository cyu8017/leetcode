// LeetCode 3979 - Maximum Valid Pair Sum
// https://leetcode.com/problems/maximum-valid-pair-sum/

object Solution {
  def maxValidPairSum(nums: Array[Int], k: Int): Int = {
    var ans = 0
    var x = 0
    var j = k
    while (j < nums.length) {
      val y = nums(j)
      x = math.max(x, nums(j - k))
      ans = math.max(ans, x + y)
      j += 1
    }
    ans
  }
}
