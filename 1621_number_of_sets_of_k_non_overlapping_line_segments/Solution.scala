// LeetCode 1621 - Number of Sets of K Non-Overlapping Line Segments
// https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

object Solution {
  def numberOfSets(n: Int, k: Int): Int = {
    val MOD = 1000000007
    def comb(nn: Int, rr: Int): Long = {
      if (rr < 0 || rr > nn) return 0L
      var res = 1L
      val r = math.min(rr, nn - rr)
      var i = 0
      while (i < r) {
        res = res * (nn - i) / (i + 1)
        i += 1
      }
      res
    }
    (comb(n + k - 1, 2 * k) % MOD).toInt
  }
}
