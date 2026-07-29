// LeetCode 1041 - Robot Bounded In Circle
// https://leetcode.com/problems/robot-bounded-in-circle/

object Solution {
  def isRobotBounded(instructions: String): Boolean = {
    var x = 0
    var y = 0
    var dx = 0
    var dy = 1
    for (ch <- instructions) {
      if (ch == 'G') {
        x += dx
        y += dy
      } else if (ch == 'L') {
        val ndx = -dy
        dy = dx
        dx = ndx
      } else {
        val ndx = dy
        dy = -dx
        dx = ndx
      }
    }
    (x == 0 && y == 0) || !(dx == 0 && dy == 1)
  }
}
