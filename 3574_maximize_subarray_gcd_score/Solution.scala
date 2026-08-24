// LeetCode 3574 - Maximize Subarray GCD Score
// https://leetcode.com/problems/maximize-subarray-gcd-score/

object Solution {
  def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) { val t = a % b; a = b; b = t }
    a
  }

  def maxGCDScore(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val cnt = new Array[Int](n)
    var i = 0
    while (i < n) {
      var x = nums(i)
      while (x % 2 == 0) { cnt(i) += 1; x /= 2 }
      i += 1
    }
    var ans = 0L
    var l = 0
    while (l < n) {
      var g = 0
      var mi = Integer.MAX_VALUE
      var t = 0
      var r = l
      while (r < n) {
        g = gcd(g, nums(r))
        if (cnt(r) < mi) { mi = cnt(r); t = 1 }
        else if (cnt(r) == mi) t += 1
        var score = 1L * g * (r - l + 1)
        if (t <= k) score *= 2
        ans = math.max(ans, score)
        r += 1
      }
      l += 1
    }
    ans
  }
}
