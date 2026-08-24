// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum_partition_score/

object Solution {
  private var prefix: Array[Long] = _
  private var previous: Array[Long] = _
  private var current: Array[Long] = _
  private val INF = 1L << 62

  def minPartitionScore(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    prefix = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + nums(i)
      i += 1
    }
    previous = Array.fill(n + 1)(INF)
    previous(0) = 0
    var parts = 1
    while (parts <= k) {
      current = Array.fill(n + 1)(INF)
      compute(parts, n, parts - 1, n - 1)
      previous = current
      parts += 1
    }
    previous(n)
  }

  private def value(left: Int, right: Int): Long = {
    val sum = prefix(right) - prefix(left)
    sum * (sum + 1) / 2
  }

  private def compute(lo: Int, hi: Int, optLo: Int, optHi: Int): Unit = {
    if (lo > hi) return
    val mid = (lo + hi) / 2
    var bestIndex = -1
    val end = math.min(optHi, mid - 1)
    var split = optLo
    while (split <= end) {
      if (previous(split) != INF) {
        val candidate = previous(split) + value(split, mid)
        if (candidate < current(mid)) {
          current(mid) = candidate
          bestIndex = split
        }
      }
      split += 1
    }
    if (bestIndex == -1) bestIndex = optLo
    compute(lo, mid - 1, optLo, bestIndex)
    compute(mid + 1, hi, bestIndex, optHi)
  }
}
