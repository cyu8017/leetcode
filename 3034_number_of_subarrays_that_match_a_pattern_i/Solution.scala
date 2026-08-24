// LeetCode 3034 - Number of Subarrays That Match a Pattern I
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

object Solution {
  private def f(a: Int, b: Int): Int = {
    if (a == b) 0 else if (a < b) 1 else -1
  }

  def countMatchingSubarrays(nums: Array[Int], pattern: Array[Int]): Int = {
    val n = nums.length
    val m = pattern.length
    var ans = 0
    var i = 0
    while (i < n - m) {
      var ok = 1
      var k = 0
      while (k < m && ok != 0) {
        if (f(nums(i + k), nums(i + k + 1)) != pattern(k)) ok = 0
        k += 1
      }
      ans += ok
      i += 1
    }
    ans
  }
}
