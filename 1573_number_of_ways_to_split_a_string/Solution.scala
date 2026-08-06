// LeetCode 1573 - Number of Ways to Split a String
// https://leetcode.com/problems/number-of-ways-to-split-a-string/

object Solution {
  def numWays(s: String): Int = {
    val MOD = 1000000007L
    val ones = s.count(_ == '1')
    if (ones % 3 != 0) return 0
    if (ones == 0) {
      val gaps = s.length - 1L
      return ((gaps * (gaps - 1) / 2) % MOD).toInt
    }
    val target = ones / 3
    val positions = s.zipWithIndex.collect { case (ch, i) if ch == '1' => i }
    (((positions(target) - positions(target - 1)).toLong * (positions(2 * target) - positions(2 * target - 1))) % MOD).toInt
  }
}
