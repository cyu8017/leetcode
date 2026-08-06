// LeetCode 1923 - Longest Common Subpath
// https://leetcode.com/problems/longest-common-subpath/

object Solution {
  def longestCommonSubpath(n: Int, paths: Array[Array[Int]]): Int = {
    val BASE1 = 911382323L
    val MOD1 = 1000000007L
    val BASE2 = 972663749L
    val MOD2 = 1000000009L

    def modPow(base: Long, exp: Int, mod: Long): Long = {
      var b = base % mod
      var e = exp
      var res = 1L
      while (e > 0) {
        if ((e & 1) == 1) res = res * b % mod
        b = b * b % mod
        e >>= 1
      }
      res
    }

    def hasCommon(length: Int): Boolean = {
      if (length == 0) return true
      var common: Option[Set[(Long, Long)]] = None
      val pow1 = modPow(BASE1, length, MOD1)
      val pow2 = modPow(BASE2, length, MOD2)
      for (path <- paths) {
        if (path.length < length) return false
        var h1 = 0L
        var h2 = 0L
        val seen = scala.collection.mutable.Set.empty[(Long, Long)]
        for (i <- path.indices) {
          h1 = (h1 * BASE1 + path(i) + 1) % MOD1
          h2 = (h2 * BASE2 + path(i) + 1) % MOD2
          if (i >= length) {
            h1 = (h1 - (path(i - length) + 1L) * pow1 % MOD1 + MOD1) % MOD1
            h2 = (h2 - (path(i - length) + 1L) * pow2 % MOD2 + MOD2) % MOD2
          }
          if (i >= length - 1) seen += ((h1, h2))
        }
        common = common match {
          case None => Some(seen.toSet)
          case Some(c) =>
            val next = c.intersect(seen)
            if (next.isEmpty) return false
            Some(next)
        }
      }
      true
    }

    var lo = 0
    var hi = paths.map(_.length).min
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (hasCommon(mid)) lo = mid
      else hi = mid - 1
    }
    lo
  }
}
