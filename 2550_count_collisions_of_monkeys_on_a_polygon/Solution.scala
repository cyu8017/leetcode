// LeetCode 2550 - Count Collisions of Monkeys on a Polygon
// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

object Solution {
  private val MOD = 1000000007

  def monkeyMove(n: Int): Int = {
    (powMod(2, n) - 2 + MOD) % MOD
  }

  private def powMod(a0: Long, e0: Int): Int = {
    var res = 1L
    var a = a0
    var e = e0
    while (e > 0) {
      if ((e & 1) != 0) res = res * a % MOD
      a = a * a % MOD
      e >>= 1
    }
    res.toInt
  }
}
