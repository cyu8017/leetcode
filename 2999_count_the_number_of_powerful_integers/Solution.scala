// LeetCode 2999 - Count the Number of Powerful Integers
// https://leetcode.com/problems/count-the-number-of-powerful-integers/

object Solution {
  def numberOfPowerfulInt(start: Long, finish: Long, limit: Int, s: String): Long = {
    def count(num: Long): Long = {
      if (num < 0) return 0
      var i = 0
      while (i < s.length) {
        if (s.charAt(i) - '0' > limit) return 0
        i += 1
      }
      val t = num.toString
      val n = t.length
      val sn = s.length
      if (n < sn) return 0
      var ans = 0L
      var length = sn
      while (length < n) {
        val preLen = length - sn
        if (preLen == 0) ans += 1
        else {
          var ways = limit.toLong
          var j = 1
          while (j < preLen) { ways *= (limit + 1); j += 1 }
          ans += ways
        }
        length += 1
      }
      val pref = n - sn
      val memo = scala.collection.mutable.HashMap[Long, Long]()
      def dfs(i: Int, tight: Boolean): Long = {
        if (i == pref) {
          if (tight) return if (t.substring(pref).compareTo(s) >= 0) 1 else 0
          return 1
        }
        val key = (i.toLong << 1) | (if (tight) 1 else 0)
        if (memo.contains(key)) return memo(key)
        var up = if (tight) t.charAt(i) - '0' else limit
        if (up > limit) up = limit
        var res = 0L
        var d = 0
        while (d <= up) {
          if (!(i == 0 && d == 0)) res += dfs(i + 1, tight && d == (t.charAt(i) - '0'))
          d += 1
        }
        memo(key) = res
        res
      }
      ans += dfs(0, true)
      ans
    }
    count(finish) - count(start - 1)
  }
}
