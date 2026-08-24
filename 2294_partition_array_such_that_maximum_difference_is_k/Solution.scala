// LeetCode 2294 - Partition Array Such That Maximum Difference Is K
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

object Solution {
  def partitionArray(nums: Array[Int], k: Int): Int = {
    java.util.Arrays.sort(nums)
    var ans = 1
    var start = nums(0)
    var i = 1
    while (i < nums.length) {
      if (nums(i) - start > k) {
        ans += 1
        start = nums(i)
      }
      i += 1
    }
    ans
  }
}
