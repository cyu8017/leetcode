// LeetCode 2302 - Count Subarrays With Score Less Than K
// https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

object Solution {
  def countSubarrays(nums: Array[Int], k: Long): Long = {
    var ans = 0L
    var sum = 0L
    var left = 0
    var right = 0
    while (right < nums.length) {
      sum += nums(right)
      while (sum * (right - left + 1) >= k) {
        sum -= nums(left)
        left += 1
      }
      ans += right - left + 1
      right += 1
    }
    ans
  }
}
