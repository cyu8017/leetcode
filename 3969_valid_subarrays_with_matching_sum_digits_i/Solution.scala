// LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

object Solution {
  def countValidSubarrays(nums: Array[Int], x: Int): Int = {
    val n = nums.length
    var ans = 0
    var l = 0
    while (l < n) {
      var s = 0L
      var r = l
      while (r < n) {
        s += nums(r)
        if (s % 10 == x) {
          val t = s.toString
          if (t.charAt(0) - '0' == x) ans += 1
        }
        r += 1
      }
      l += 1
    }
    ans
  }
}
