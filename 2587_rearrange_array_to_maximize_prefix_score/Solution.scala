// LeetCode 2587 - Rearrange Array to Maximize Prefix Score
// https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

object Solution {
  def maxScore(nums: Array[Int]): Int = {
    java.util.Arrays.sort(nums)
    var sum = 0L
    var ans = 0
    var i = nums.length - 1
    while (i >= 0) {
      sum += nums(i)
      if (sum > 0) ans += 1
      else return ans
      i -= 1
    }
    ans
  }
}
