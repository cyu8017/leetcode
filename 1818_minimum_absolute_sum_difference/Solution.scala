// LeetCode 1818 - Minimum Absolute Sum Difference
// https://leetcode.com/problems/minimum-absolute-sum-difference/

object Solution {
  def minAbsoluteSumDiff(nums1: Array[Int], nums2: Array[Int]): Int = {
    val MOD = 1000000007
    val sorted = nums1.sorted
    var total = 0L
    var bestGain = 0
    for (i <- nums1.indices) {
      val current = math.abs(nums1(i) - nums2(i))
      total += current
      val target = nums2(i)
      var lo = 0
      var hi = sorted.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (sorted(mid) < target) lo = mid + 1 else hi = mid
      }
      for (j <- Seq(lo - 1, lo) if j >= 0 && j < sorted.length) {
        bestGain = math.max(bestGain, current - math.abs(sorted(j) - target))
      }
    }
    ((total - bestGain) % MOD).toInt
  }
}
