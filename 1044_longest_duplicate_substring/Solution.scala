// LeetCode 1044 - Longest Duplicate Substring
// https://leetcode.com/problems/longest-duplicate-substring/

object Solution {
  def longestDupSubstring(s: String): String = {
    val MOD = (1L << 61) - 1
    val BASE = 256L
    val n = s.length
    val nums = s.map(_.toLong).toArray

    def search(length: Int): Int = {
      if (length == 0) return 0
      var h = 0L
      for (i <- 0 until length) h = (h * BASE + nums(i)) % MOD
      val seen = scala.collection.mutable.Map[Long, scala.collection.mutable.ArrayBuffer[Int]]()
      seen(h) = scala.collection.mutable.ArrayBuffer(0)
      var power = 1L
      for (_ <- 0 until length) power = (power * BASE) % MOD
      for (i <- 1 to n - length) {
        h = (h * BASE - nums(i - 1) * power % MOD + MOD) % MOD
        h = (h + nums(i + length - 1)) % MOD
        if (seen.contains(h)) {
          val cur = s.substring(i, i + length)
          for (j <- seen(h)) {
            if (s.substring(j, j + length) == cur) return i
          }
          seen(h) += i
        } else {
          seen(h) = scala.collection.mutable.ArrayBuffer(i)
        }
      }
      -1
    }

    var lo = 0
    var hi = n - 1
    var start = -1
    var bestLen = 0
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      val pos = search(mid)
      if (pos >= 0) {
        start = pos
        bestLen = mid
        lo = mid + 1
      } else {
        hi = mid - 1
      }
    }
    if (start >= 0) s.substring(start, start + bestLen) else ""
  }
}
