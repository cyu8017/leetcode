// LeetCode 3095 - Shortest Subarray With OR at Least K I
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/

object Solution {
  def minimumSubarrayLength(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val cnt = new Array[Int](32)
    var ans = n + 1
    var s = 0
    var i = 0
    var j = 0
    while (j < n) {
      val x = nums(j)
      s |= x
      var h = 0
      while (h < 32) {
        if (((x >> h) & 1) != 0) cnt(h) += 1
        h += 1
      }
      while (s >= k && i <= j) {
        ans = math.min(ans, j - i + 1)
        h = 0
        while (h < 32) {
          if (((nums(i) >> h) & 1) != 0) {
            cnt(h) -= 1
            if (cnt(h) == 0) s ^= 1 << h
          }
          h += 1
        }
        i += 1
      }
      j += 1
    }
    if (ans == n + 1) -1 else ans
  }
}
