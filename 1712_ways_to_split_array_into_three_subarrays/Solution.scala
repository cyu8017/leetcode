// LeetCode 1712 - Ways to Split Array Into Three Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

object Solution {
  def waysToSplit(nums: Array[Int]): Int = {
    val mod = 1000000007L
    val n = nums.length
    val prefix = new Array[Long](n)
    var total = 0L
    for (i <- nums.indices) {
      total += nums(i)
      prefix(i) = total
    }

    def lowerBound(target: Long, start: Int, end: Int): Int = {
      var lo = start
      var hi = end
      while (lo < hi) {
        val mid = (lo + hi) >>> 1
        if (prefix(mid) < target) lo = mid + 1 else hi = mid
      }
      lo
    }

    def upperBound(target: Long, start: Int, end: Int): Int = {
      var lo = start
      var hi = end
      while (lo < hi) {
        val mid = (lo + hi) >>> 1
        if (prefix(mid) <= target) lo = mid + 1 else hi = mid
      }
      lo
    }

    var ans = 0L
    for (i <- 0 until n - 2) {
      val left = prefix(i)
      val lo = lowerBound(2 * left, i + 1, n - 1)
      val hi = upperBound((total + left) / 2, lo, n - 1)
      ans = (ans + hi - lo) % mod
    }
    ans.toInt
  }
}
