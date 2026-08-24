// LeetCode 2543 - Check if Point Is Reachable
// https://leetcode.com/problems/check-if-point-is-reachable/

object Solution {
  def isReachable(targetX: Int, targetY: Int): Boolean = {
    var g = gcd(targetX, targetY)
    while (g % 2 == 0) g /= 2
    g == 1
  }

  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }
}
