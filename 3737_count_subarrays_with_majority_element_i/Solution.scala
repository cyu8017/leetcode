// LeetCode 3737 - Count Subarrays With Majority Element I
// https://leetcode.com/problems/count-subarrays-with-majority-element-i/

object Solution {
  def countMajoritySubarrays(nums: Array[Int], target: Int): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      var cnt = 0
      var j = i
      while (j < n) {
        if (nums(j) == target) cnt += 1
        if (cnt * 2 > j - i + 1) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
