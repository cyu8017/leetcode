// LeetCode 3207 - Maximum Points After Enemy Battles
// https://leetcode.com/problems/maximum-points-after-enemy-battles/

object Solution {
  def maximumPoints(enemyEnergies: Array[Int], currentEnergy: Int): Long = {
    java.util.Arrays.sort(enemyEnergies)
    if (currentEnergy < enemyEnergies(0)) return 0L
    var ans = 0L
    var energy = currentEnergy
    var i = enemyEnergies.length - 1
    while (i >= 0) {
      ans += energy / enemyEnergies(0)
      energy %= enemyEnergies(0)
      energy += enemyEnergies(i)
      i -= 1
    }
    ans
  }
}
