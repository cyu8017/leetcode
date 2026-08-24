// LeetCode 0780 - Reaching Points
// https://leetcode.com/problems/reaching-points/

object Solution {
  def reachingPoints(sx: Int, sy: Int, tx: Int, ty: Int): Boolean = {
    var x = tx
    var y = ty
    while (x >= sx && y >= sy) {
      if (x == sx && y == sy) return true
      if (x == y) return false
      if (x > y) {
        if (y > sy) x %= y
        else return (x - sx) % y == 0
      } else {
        if (x > sx) y %= x
        else return (y - sy) % x == 0
      }
    }
    x == sx && y == sy
  }
}
