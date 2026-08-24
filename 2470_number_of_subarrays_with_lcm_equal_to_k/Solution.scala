// LeetCode 2470 - Number of Subarrays With LCM Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

object Solution {
  def subarrayLCM(nums: Array[Int], k: Int): Int = {
    def gcd(x: Int, y: Int): Int = {
      var a = x
      var b = y
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    var ans = 0
    val n = nums.length
    var i = 0
    while (i < n) {
      var cur = 1L
      var j = i
      var cont = true
      while (j < n && cont) {
        cur = cur / gcd(cur.toInt, nums(j)) * nums(j)
        if (cur > k) cont = false
        else {
          if (cur == k) ans += 1
          j += 1
        }
      }
      i += 1
    }
    ans
  }
}
