// LeetCode 0542 - 01 Matrix
// https://leetcode.com/problems/01-matrix/

import scala.collection.mutable

object Solution {
  def updateMatrix(mat: Array[Array[Int]]): Array[Array[Int]] = {
    val rows = mat.length
    val cols = mat(0).length
    val dist = Array.fill(rows, cols)(1000000000)
    val queue = mutable.Queue[(Int, Int)]()

    for (row <- 0 until rows; col <- 0 until cols) {
      if (mat(row)(col) == 0) {
        dist(row)(col) = 0
        queue.enqueue((row, col))
      }
    }

    val directions = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    while (queue.nonEmpty) {
      val (row, col) = queue.dequeue()
      for ((dr, dc) <- directions) {
        val nr = row + dr
        val nc = col + dc
        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && dist(nr)(nc) > dist(row)(col) + 1) {
          dist(nr)(nc) = dist(row)(col) + 1
          queue.enqueue((nr, nc))
        }
      }
    }

    dist
  }
}
