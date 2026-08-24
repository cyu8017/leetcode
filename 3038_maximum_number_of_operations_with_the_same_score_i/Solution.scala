// LeetCode 3038 - Maximum Number of Operations With the Same Score I
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

object Solution {
  def maxOperations(nums: Array[Int]): Int = {
    val s = nums(0) + nums(1)
    val n = nums.length
    var ans = 0
    var i = 0
    while (i + 1 < n && nums(i) + nums(i + 1) == s) {
      ans += 1
      i += 2
    }
    ans
  }
}
