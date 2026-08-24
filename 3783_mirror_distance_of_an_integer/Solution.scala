// LeetCode 3783 - Mirror Distance Of An Integer
// https://leetcode.com/problems/mirror-distance-of-an-integer/

object Solution {
  def mirrorDistance(n: Int): Int = math.abs(n - reverse(n))

  private def reverse(x0: Int): Int = {
    var x = x0
    var y = 0
    while (x > 0) {
      y = y * 10 + x % 10
      x /= 10
    }
    y
  }
}
