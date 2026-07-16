// LeetCode 0490 - The Maze
// https://leetcode.com/problems/the-maze/

import scala.collection.mutable

object Solution {
  def hasPath(maze: Array[Array[Int]], start: Array[Int], destination: Array[Int]): Boolean = {
    val rows = maze.length
    val cols = maze(0).length
    val directions = Array(Array(-1, 0), Array(1, 0), Array(0, -1), Array(0, 1))
    val visited = mutable.Set.empty[String]
    val stack = mutable.ArrayBuffer(Array(start(0), start(1)))

    while (stack.nonEmpty) {
      val cell = stack.remove(stack.length - 1)
      val row = cell(0)
      val col = cell(1)
      val key = s"$row,$col"
      if (!visited.contains(key)) {
        visited.add(key)
        if (row == destination(0) && col == destination(1)) return true
        directions.foreach { direction =>
          val dr = direction(0)
          val dc = direction(1)
          var nr = row
          var nc = col
          while (nr + dr >= 0 && nr + dr < rows && nc + dc >= 0 && nc + dc < cols && maze(nr + dr)(nc + dc) == 0) {
            nr += dr
            nc += dc
          }
          val nextKey = s"$nr,$nc"
          if (!visited.contains(nextKey)) stack += Array(nr, nc)
        }
      }
    }
    false
  }
}
