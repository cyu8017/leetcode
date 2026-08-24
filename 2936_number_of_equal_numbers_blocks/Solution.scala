// LeetCode 2936 - Number of Equal Numbers Blocks
// https://leetcode.com/problems/number-of-equal-numbers-blocks/

object Solution {
  def blockCount(nums: Array[Int]): Int = {
    if (nums.isEmpty) return 0
    var ans = 1
    for (i <- 1 until nums.length if nums(i) != nums(i - 1)) ans += 1
    ans
  }
}
