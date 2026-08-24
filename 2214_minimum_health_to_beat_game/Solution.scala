// LeetCode 2214 - Minimum Health to Beat Game
// https://leetcode.com/problems/minimum-health-to-beat-game/

object Solution {
  def minimumHealth(damage: Array[Int], armor: Int): Long = {
    var sum = 0L
    var mx = 0
    for (d <- damage) {
      sum += d
      mx = math.max(mx, d)
    }
    sum - math.min(armor, mx) + 1
  }
}
