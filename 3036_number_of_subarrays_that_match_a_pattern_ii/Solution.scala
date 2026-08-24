// LeetCode 3036 - Number of Subarrays That Match a Pattern II
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/

object Solution {
  def countMatchingSubarrays(nums: Array[Int], pattern: Array[Int]): Int = {
    val N = pattern.length
    val ps = Array.ofDim[Int](N + 1)
    ps(0) = -1
    ps(1) = 0
    var i = 2
    var p = 0
    while (i <= N) {
      val x = pattern(i - 1)
      while (p >= 0 && pattern(p) != x) p = ps(p)
      p += 1
      ps(i) = p
      i += 1
    }
    var res = 0
    val M = nums.length
    i = 1
    p = 0
    while (i < M) {
      var t = nums(i) - nums(i - 1)
      if (t > 0) t = 1
      else if (t < 0) t = -1
      while (p >= 0 && pattern(p) != t) p = ps(p)
      p += 1
      if (p == N) {
        res += 1
        p = ps(p)
      }
      i += 1
    }
    res
  }
}
