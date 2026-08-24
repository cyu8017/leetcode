// LeetCode 2369 - Check if There is a Valid Partition For The Array
// https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

object Solution {
  def validPartition(nums: Array[Int]): Boolean = {
    val n = nums.length
    val dp = Array.fill(n + 1)(false)
    dp(0) = true
    var i = 1
    while (i <= n) {
      if (i >= 2 && nums(i - 1) == nums(i - 2) && dp(i - 2)) dp(i) = true
      if (i >= 3 && nums(i - 1) == nums(i - 2) && nums(i - 2) == nums(i - 3) && dp(i - 3)) dp(i) = true
      if (i >= 3 && nums(i - 1) == nums(i - 2) + 1 && nums(i - 2) == nums(i - 3) + 1 && dp(i - 3)) dp(i) = true
      i += 1
    }
    dp(n)
  }
}
