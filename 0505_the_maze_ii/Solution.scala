// LeetCode 0505 - The Maze II
// https://leetcode.com/problems/the-maze-ii/

import scala.collection.mutable

object Solution {
  private case class State(dist: Int, row: Int, col: Int) extends Ordered[State] {
    override def compare(that: State): Int = dist.compareTo(that.dist)
  }

  private implicit object StateOrdering extends Ordering[State] {
    override def compare(x: State, y: State): Int = y.compare(x)
  }

  def shortestDistance(maze: Array[Array[Int]], start: Array[Int], destination: Array[Int]): Int = {
    val rows = maze.length
    val cols = maze(0).length
    val targetRow = destination(0)
    val targetCol = destination(1)
    val directions = Array((-1, 0), (1, 0), (0, -1), (0, 1))
    val best = mutable.Map.empty[String, Int]
    val heap = mutable.PriorityQueue.empty[State]
    heap.enqueue(State(0, start(0), start(1)))

    while (heap.nonEmpty) {
      val current = heap.dequeue()
      if (current.row == targetRow && current.col == targetCol) return current.dist
      val stateKey = s"${current.row},${current.col}"
      if (best.get(stateKey).exists(_ <= current.dist)) ()
      else {
        best(stateKey) = current.dist
        for ((dr, dc) <- directions) {
          var nextRow = current.row
          var nextCol = current.col
          var traveled = 0
          while (
            nextRow + dr >= 0 && nextRow + dr < rows
            && nextCol + dc >= 0 && nextCol + dc < cols
            && maze(nextRow + dr)(nextCol + dc) == 0
          ) {
            nextRow += dr
            nextCol += dc
            traveled += 1
          }
          if (nextRow != current.row || nextCol != current.col) {
            val newDist = current.dist + traveled
            val targetKey = s"$nextRow,$nextCol"
            if (!best.contains(targetKey) || newDist < best(targetKey)) {
              heap.enqueue(State(newDist, nextRow, nextCol))
            }
          }
        }
      }
    }
    -1
  }
}
