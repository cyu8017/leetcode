// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

object Solution {
  private def bitsPop(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x > 0) { c += x & 1; x >>= 1 }
    c
  }

  def countKReducibleNumbers(s: String, k: Int): Int = {
    val mod = 1000000007
    val red = new Array[Int](801)
    red(1) = 0
    var i = 2
    while (i <= 800) {
      red(i) = 1 + red(bitsPop(i))
      i += 1
    }
    val memo = scala.collection.mutable.HashMap.empty[Long, Int]
    def key(pos: Int, tight: Int, ones: Int): Long =
      (pos.toLong << 32) | (tight.toLong << 16) | ones
    def dfs(pos: Int, tight: Boolean, ones: Int): Int = {
      if (pos == s.length) {
        if (ones == 0) return 0
        return if (red(ones) <= k - 1) 1 else 0
      }
      val ky = key(pos, if (tight) 1 else 0, ones)
      if (memo.contains(ky)) return memo(ky)
      val up = if (tight) s.charAt(pos) - '0' else 1
      var ans = 0
      var d = 0
      while (d <= up) {
        val nt = tight && d == up
        ans = (ans + dfs(pos + 1, nt, ones + d)) % mod
        d += 1
      }
      memo(ky) = ans
      ans
    }
    dfs(0, true, 0)
  }
}
