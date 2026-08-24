// LeetCode 3795 - Minimum Subarray Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/

object Solution {
  def minLength(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    var ans = n + 1
    var l = 0
    val cnt = new java.util.HashMap[Integer, Integer]()
    var s = 0L
    var r = 0
    while (r < n) {
      val c = cnt.merge(nums(r), 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
      if (c == 1) s += nums(r)
      while (s >= k) {
        if (r - l + 1 < ans) ans = r - l + 1
        val left = nums(l)
        val nc = cnt.merge(left, -1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
        if (nc == 0) {
          cnt.remove(left)
          s -= left
        }
        l += 1
      }
      r += 1
    }
    if (ans > n) -1 else ans
  }
}
