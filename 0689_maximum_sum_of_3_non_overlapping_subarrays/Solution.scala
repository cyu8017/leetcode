// LeetCode 0689 - Maximum Sum of 3 Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

object Solution {
  def maxSumOfThreeSubarrays(nums: Array[Int], k: Int): Array[Int] = {
    val n = nums.length
    val windows = n - k + 1
    val sums = Array.ofDim[Int](windows)
    var total = 0
    var i = 0
    while (i < k) {
      total += nums(i)
      i += 1
    }
    sums(0) = total
    i = 1
    while (i < windows) {
      total += nums(i + k - 1) - nums(i - 1)
      sums(i) = total
      i += 1
    }
    val left = Array.ofDim[Int](windows)
    var best = 0
    i = 0
    while (i < windows) {
      if (sums(i) > sums(best)) best = i
      left(i) = best
      i += 1
    }
    val right = Array.ofDim[Int](windows)
    best = windows - 1
    i = windows - 1
    while (i >= 0) {
      if (sums(i) >= sums(best)) best = i
      right(i) = best
      i -= 1
    }
    var answer = Array(0, 0, 0)
    var bestTotal = -1
    var mid = k
    while (mid < windows - k) {
      val l = left(mid - k)
      val r = right(mid + k)
      val cur = sums(l) + sums(mid) + sums(r)
      if (cur > bestTotal) {
        bestTotal = cur
        answer = Array(l, mid, r)
      }
      mid += 1
    }
    answer
  }
}
