// LeetCode 0499 - The Maze III
// https://leetcode.com/problems/the-maze-iii/

import scala.collection.mutable

object Solution {
  private case class Best(dist: Int, path: String)
  private case class State(dist: Int, path: String, row: Int, col: Int) extends Ordered[State] {
    override def compare(that: State): Int = {
      if (dist != that.dist) dist.compareTo(that.dist)
      else path.compare(that.path)
    }
  }

  private implicit object StateOrdering extends Ordering[State] {
    override def compare(x: State, y: State): Int = y.compare(x)
  }

  def findShortestWay(maze: Array[Array[Int]], ball: Array[Int], hole: Array[Int]): String = {
    val rows = maze.length
    val cols = maze(0).length
    val holeRow = hole(0)
    val holeCol = hole(1)
    val directions = Array((1, 0), (0, -1), (0, 1), (-1, 0))
    val labels = Array("d", "l", "r", "u")
    val best = mutable.Map.empty[String, Best]
    val heap = mutable.PriorityQueue.empty[State]
    heap.enqueue(State(0, "", ball(0), ball(1)))

    while (heap.nonEmpty) {
      val current = heap.dequeue()
      val stateKey = s"${current.row},${current.col}"
      best.get(stateKey) match {
        case Some(recorded)
            if current.dist > recorded.dist
              || (current.dist == recorded.dist && current.path.compare(recorded.path) >= 0) =>
          ()
        case _ =>
          best(stateKey) = Best(current.dist, current.path)
          if (current.row == holeRow && current.col == holeCol) return current.path
          for (direction <- directions.indices) {
            val (dr, dc) = directions(direction)
            var nextRow = current.row
            var nextCol = current.col
            var traveled = 0
            var rolling = true
            while (
              rolling
              && nextRow + dr >= 0 && nextRow + dr < rows
              && nextCol + dc >= 0 && nextCol + dc < cols
              && maze(nextRow + dr)(nextCol + dc) == 0
            ) {
              nextRow += dr
              nextCol += dc
              traveled += 1
              if (nextRow == holeRow && nextCol == holeCol) rolling = false
            }
            if (nextRow != current.row || nextCol != current.col) {
              val newDist = current.dist + traveled
              val newPath = current.path + labels(direction)
              val targetKey = s"$nextRow,$nextCol"
              val shouldEnqueue = best.get(targetKey) match {
                case None => true
                case Some(existing)
                    if newDist < existing.dist
                      || (newDist == existing.dist && newPath.compare(existing.path) < 0) =>
                  true
                case Some(_) => false
              }
              if (shouldEnqueue) heap.enqueue(State(newDist, newPath, nextRow, nextCol))
            }
          }
      }
    }
    "impossible"
  }
}
