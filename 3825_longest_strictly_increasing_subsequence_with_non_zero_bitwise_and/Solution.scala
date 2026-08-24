// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non Zero Bitwise And
// https://leetcode.com/problems/longest_strictly_increasing_subsequence_with_non_zero_bitwise_and/

object Solution {
  private def bitLen(x0: Int): Int = {
    var x = x0
    if (x == 0) return 0
    var n = 0
    while (x > 0) { n += 1; x >>= 1 }
    n
  }

  private def lis(arr: scala.collection.mutable.ArrayBuffer[Int]): Int = {
    val g = scala.collection.mutable.ArrayBuffer.empty[Int]
    arr.foreach { x =>
      var lo = 0
      var hi = g.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (g(mid) < x) lo = mid + 1
        else hi = mid
      }
      if (lo == g.length) g += x
      else g(lo) = x
    }
    g.length
  }

  def longestSubsequence(nums: Array[Int]): Int = {
    var ans = 0
    var mx = 0
    nums.foreach { x => mx = math.max(mx, x) }
    val m = bitLen(mx)
    var i = 0
    while (i < m) {
      val arr = scala.collection.mutable.ArrayBuffer.empty[Int]
      nums.foreach { x => if (((x >> i) & 1) != 0) arr += x }
      ans = math.max(ans, lis(arr))
      i += 1
    }
    ans
  }
}
