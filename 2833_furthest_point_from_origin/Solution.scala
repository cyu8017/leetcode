// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

object Solution {
  def furthestDistanceFromOrigin(moves: String): Int = {
    var L = 0
    var R = 0
    var u = 0
    moves.foreach { c =>
      if (c == 'L') L += 1
      else if (c == 'R') R += 1
      else u += 1
    }
    math.abs(L - R) + u
  }
}
