// LeetCode 2576 - Find the Maximum Number of Marked Indices
// https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

object Solution {
  def maxNumOfMarkedIndices(nums: Array[Int]): Int = {
    java.util.Arrays.sort(nums)
    val n = nums.length
    var i = 0
    var ans = 0
    var j = (n + 1) / 2
    while (j < n) {
      if (2 * nums(i) <= nums(j)) {
        ans += 2
        i += 1
      }
      j += 1
    }
    ans
  }
}
