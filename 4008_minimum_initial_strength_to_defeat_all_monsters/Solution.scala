// LeetCode 4008 - Minimum Initial Strength to Defeat All Monsters
// https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/

object Solution {
  def minInitialStrength(monsters: Array[Int], boosts: Array[Array[Int]]): Long = {
    val n = monsters.length
    val d = new Array[Long](n + 1)
    for (b <- boosts) {
      d(b(0)) += b(2)
      d(b(1) + 1) -= b(2)
    }
    var left = 0L
    var right = 1000000000000000L
    while (left < right) {
      val mid = (left + right) / 2
      if (check(mid, monsters, d)) right = mid
      else left = mid + 1
    }
    left
  }

  private def check(v0: Long, monsters: Array[Int], d: Array[Long]): Boolean = {
    var v = v0
    var bonus = 0L
    var i = 0
    while (i < monsters.length) {
      bonus += d(i)
      if (v + bonus < monsters(i)) return false
      v -= monsters(i)
      if (v < 0) v = 0
      i += 1
    }
    true
  }
}
