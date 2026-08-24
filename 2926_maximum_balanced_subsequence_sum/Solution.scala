// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

object Solution {
  private var bit: Array[Long] = _
  private val NEG_INF = -(1L << 60)

  def maxBalancedSubsequenceSum(nums: Array[Int]): Long = {
    val n = nums.length
    val keys = Array.tabulate(n)(i => nums(i) - i)
    val uniq = keys.sorted.distinct
    bit = Array.fill(uniq.length + 2)(NEG_INF)
    var ans = NEG_INF
    for (i <- 0 until n) {
      val id = idxOf(uniq, keys(i))
      val best = query(id)
      var cur = nums(i).toLong
      if (best > NEG_INF / 2) {
        val cand = best + nums(i)
        if (cand > cur) cur = cand
      }
      update(id, cur)
      if (cur > ans) ans = cur
    }
    ans
  }

  private def idxOf(uniq: Array[Int], v: Int): Int = {
    var lo = 0
    var hi = uniq.length
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (uniq(mid) < v) lo = mid + 1
      else hi = mid
    }
    lo + 1
  }

  private def update(i0: Int, value: Long): Unit = {
    var i = i0
    while (i < bit.length) {
      if (value > bit(i)) bit(i) = value
      i += i & -i
    }
  }

  private def query(i0: Int): Long = {
    var best = NEG_INF
    var i = i0
    while (i > 0) {
      if (bit(i) > best) best = bit(i)
      i -= i & -i
    }
    best
  }
}
