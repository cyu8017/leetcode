// LeetCode 2962 - Count Subarrays Where Max Element Appears at Least K Times
// https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

object Solution {
  def countSubarrays(nums: Array[Int], k: Int): Long = {
    var mx = nums(0)
    for (v <- nums) if (v > mx) mx = v
    var ans = 0L
    var cnt = 0
    var left = 0
    var right = 0
    while (right < nums.length) {
      if (nums(right) == mx) cnt += 1
      while (cnt >= k) {
        if (nums(left) == mx) cnt -= 1
        left += 1
      }
      ans += left
      right += 1
    }
    ans
  }
}
