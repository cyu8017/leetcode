// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

object Solution {
  def upperBound(a: java.util.ArrayList[Integer], target: Int): Int = {
    var lo = 0
    var hi = a.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a.get(mid) <= target) lo = mid + 1
      else hi = mid
    }
    lo
  }

  def countInv(nums: Array[Int], k: Int, threshold: Int): Boolean = {
    val sorted = new java.util.ArrayList[Integer]()
    var inv = 0L
    for (num <- nums) {
      val left = upperBound(sorted, num)
      val right = upperBound(sorted, num + threshold)
      inv += right - left
      sorted.add(upperBound(sorted, num), num)
    }
    inv >= k
  }

  def minThreshold(nums: Array[Int], k: Int): Int = {
    var mx = 0
    for (v <- nums) if (v > mx) mx = v
    var l = 0
    var r = mx + 1
    while (l < r) {
      val m = (l + r) / 2
      if (countInv(nums, k, m)) r = m
      else l = m + 1
    }
    if (l > mx) -1 else l
  }
}
