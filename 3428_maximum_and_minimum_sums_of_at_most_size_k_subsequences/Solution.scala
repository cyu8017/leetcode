// LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

object Solution {
  def minMaxSums(nums: Array[Int], k: Int): Int = {
    val mod = 1000000007
    java.util.Arrays.sort(nums)
    val n = nums.length
    val C = Array.ofDim[Int](n + 1, k)
    var i = 0
    while (i <= n) {
      C(i)(0) = 1
      var j = 1
      while (j < k && j <= i) {
        C(i)(j) = (C(i - 1)(j) + C(i - 1)(j - 1)) % mod
        j += 1
      }
      i += 1
    }
    var ans = 0
    i = 0
    while (i < n) {
      var waysMax = 0
      var j = 0
      while (j < k && j <= i) {
        waysMax = (waysMax + C(i)(j)) % mod
        j += 1
      }
      var waysMin = 0
      val right = n - i - 1
      j = 0
      while (j < k && j <= right) {
        waysMin = (waysMin + C(right)(j)) % mod
        j += 1
      }
      ans = ((ans + nums(i).toLong * waysMax % mod + nums(i).toLong * waysMin % mod) % mod).toInt
      i += 1
    }
    ans
  }
}
