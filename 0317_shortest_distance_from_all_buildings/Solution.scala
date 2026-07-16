// LeetCode 0317 - Shortest Distance from All Buildings

// https://leetcode.com/problems/shortest-distance-from-all-buildings/



import scala.collection.mutable



object Solution {

  def shortestDistance(grid: Array[Array[Int]]): Int = {

    if (grid.isEmpty || grid(0).isEmpty) {

      return -1

    }



    val rows = grid.length

    val cols = grid(0).length

    var buildings = 0

    val distances = Array.fill(rows, cols)(0)

    val reach = Array.fill(rows, cols)(0)

    val directions = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))



    for (row <- 0 until rows; col <- 0 until cols if grid(row)(col) == 1) {

      buildings += 1

    }



    for (row <- 0 until rows; col <- 0 until cols if grid(row)(col) == 1) {

      val queue = mutable.Queue.empty[(Int, Int, Int)]

      queue.enqueue((row, col, 0))

      val visited = Array.fill(rows, cols)(false)

      visited(row)(col) = true

      while (queue.nonEmpty) {

        val (currentRow, currentCol, distance) = queue.dequeue()

        for (direction <- directions) {

          val nextRow = currentRow + direction(0)

          val nextCol = currentCol + direction(1)

          if (

            nextRow >= 0 && nextRow < rows &&

            nextCol >= 0 && nextCol < cols &&

            grid(nextRow)(nextCol) == 0 &&

            !visited(nextRow)(nextCol)

          ) {

            visited(nextRow)(nextCol) = true

            distances(nextRow)(nextCol) += distance + 1

            reach(nextRow)(nextCol) += 1

            queue.enqueue((nextRow, nextCol, distance + 1))

          }

        }

      }

    }



    var best = Int.MaxValue

    for (row <- 0 until rows; col <- 0 until cols) {

      if (grid(row)(col) == 0 && reach(row)(col) == buildings) {

        best = math.min(best, distances(row)(col))

      }

    }

    if (best == Int.MaxValue) -1 else best

  }

}

