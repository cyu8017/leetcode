// LeetCode 3685 - Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/

object Solution {
  def subsequenceSumAfterCapping(nums: Array[Int], k: Int): Array[Boolean] = {
    val n = nums.length
    val sorted = nums.clone()
    java.util.Arrays.sort(sorted)
    val ans = new Array[Boolean](n)
    val reach = new Array[Boolean](k + 1)
    reach(0) = true
    var idx = 0
    var x = 1
    while (x <= n) {
      while (idx < n && sorted(idx) <= x) {
        val v = sorted(idx)
        var s = k
        while (s >= v) {
          if (reach(s - v)) reach(s) = true
          s -= 1
        }
        idx += 1
      }
      val tmp = reach.clone()
      val rem = n - idx
      var s = 0
      while (s <= k) {
        if (reach(s)) {
          var t = 1
          while (t <= rem && s + t * x <= k) {
            tmp(s + t * x) = true
            t += 1
          }
        }
        s += 1
      }
      ans(x - 1) = tmp(k)
      x += 1
    }
    ans
  }
}
