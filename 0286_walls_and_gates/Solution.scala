// LeetCode 0286 - Walls and Gates
// https://leetcode.com/problems/walls-and-gates/

import scala.collection.mutable

object Solution {
  def wallsAndGates(rooms: Array[Array[Int]]): Unit = {
    if (rooms.isEmpty || rooms(0).isEmpty) {
      return
    }
    val rows = rooms.length
    val cols = rooms(0).length
    val queue = mutable.Queue[(Int, Int)]()
    for (row <- 0 until rows; col <- 0 until cols if rooms(row)(col) == 0) {
      queue.enqueue((row, col))
    }
    val directions = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    while (queue.nonEmpty) {
      val (row, col) = queue.dequeue()
      for ((dr, dc) <- directions) {
        val nextRow = row + dr
        val nextCol = col + dc
        if (nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols
            && rooms(nextRow)(nextCol) == 2147483647) {
          rooms(nextRow)(nextCol) = rooms(row)(col) + 1
          queue.enqueue((nextRow, nextCol))
        }
      }
    }
  }
}
