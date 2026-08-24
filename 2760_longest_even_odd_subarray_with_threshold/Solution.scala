// LeetCode 2760 - Longest Even Odd Subarray With Threshold
// https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

object Solution {
  def longestAlternatingSubarray(nums: Array[Int], threshold: Int): Int = {
    var ans = 0
    val n = nums.length
    var i = 0
    while (i < n) {
      if (nums(i) % 2 == 0 && nums(i) <= threshold) {
        var j = i
        while (j + 1 < n && nums(j + 1) <= threshold && nums(j + 1) % 2 != nums(j) % 2) j += 1
        ans = math.max(ans, j - i + 1)
      }
      i += 1
    }
    ans
  }
}
