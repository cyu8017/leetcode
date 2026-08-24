// LeetCode 0940 - Distinct Subsequences II
// https://leetcode.com/problems/distinct-subsequences-ii/

object Solution {
  def distinctSubseqII(s: String): Int = {
    val MOD = 1000000007
    val ends = Array.ofDim[Long](26)
    var total = 1L
    s.foreach { ch =>
      val prev = ends(ch - 'a')
      ends(ch - 'a') = total
      total = (total - prev + ends(ch - 'a') + MOD) % MOD
    }
    ((total - 1 + MOD) % MOD).toInt
  }
}
