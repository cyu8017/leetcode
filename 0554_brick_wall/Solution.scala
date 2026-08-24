// LeetCode 0554 - Brick Wall
// https://leetcode.com/problems/brick-wall/

import scala.collection.mutable

object Solution {
  def leastBricks(wall: List[List[Int]]): Int = {
    val edges = mutable.Map.empty[Int, Int]
    var best = 0
    wall.foreach { row =>
      var width = 0
      var i = 0
      while (i + 1 < row.size) {
        width += row(i)
        val count = edges.getOrElse(width, 0) + 1
        edges(width) = count
        best = math.max(best, count)
        i += 1
      }
    }
    wall.size - best
  }
}
