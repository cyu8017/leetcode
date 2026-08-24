// LeetCode 3632 - Subarrays With XOR At Least K
// https://leetcode.com/problems/subarrays-with-xor-at-least-k/

object Solution {
  def subarraysWithXorAtLeastK(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    var ans = 0L
    var i = 0
    while (i < n) {
      var x = 0
      var j = i
      while (j < n) {
        x ^= nums(j)
        if (x >= k) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
