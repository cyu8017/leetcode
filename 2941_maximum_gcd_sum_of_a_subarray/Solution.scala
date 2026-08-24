// LeetCode 2941 - Maximum GCD-Sum of a Subarray
// https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

object Solution {
  def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) { val t = a % b; a = b; b = t }
    a
  }

  def maxGcdSum(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val pref = Array.ofDim[Long](n + 1)
    var i = 0
    while (i < n) { pref(i + 1) = pref(i) + nums(i); i += 1 }
    var ans = 0L
    var st = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    i = 0
    while (i < n) {
      val nst = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
      nst += Array(nums(i), i)
      for (p <- st) {
        val g = gcd(p(0), nums(i))
        if (nst.last(0) != g) nst += Array(g, p(1))
      }
      st = nst
      for (p <- st) {
        val g = p(0)
        val idx = p(1)
        if (i - idx + 1 >= k) {
          val cand = (pref(i + 1) - pref(idx)) * g
          if (cand > ans) ans = cand
        }
      }
      i += 1
    }
    ans
  }
}
