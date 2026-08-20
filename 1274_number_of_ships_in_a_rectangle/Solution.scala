// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

class Point(var x: Int, var y: Int)

trait Sea {
  def hasShips(topRight: Point, bottomLeft: Point): Boolean
}

object Solution {
  def countShips(sea: Sea, topRight: Point, bottomLeft: Point): Int = {
    val tx = topRight.x
    val ty = topRight.y
    val bx = bottomLeft.x
    val by = bottomLeft.y
    if (tx < bx || ty < by || !sea.hasShips(topRight, bottomLeft)) return 0
    if (tx == bx && ty == by) return 1
    val mx = (tx + bx) / 2
    val my = (ty + by) / 2
    countShips(sea, new Point(mx, my), new Point(bx, by)) +
      countShips(sea, new Point(tx, my), new Point(mx + 1, by)) +
      countShips(sea, new Point(mx, ty), new Point(bx, my + 1)) +
      countShips(sea, new Point(tx, ty), new Point(mx + 1, my + 1))
  }
}
