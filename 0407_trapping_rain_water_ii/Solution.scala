// LeetCode 0407 - Trapping Rain Water II

// https://leetcode.com/problems/trapping-rain-water-ii/



import scala.collection.mutable



object Solution {

  def trapRainWater(heightMap: Array[Array[Int]]): Int = {

    if (heightMap.isEmpty || heightMap.head.isEmpty) {

      return 0

    }



    val rows = heightMap.length

    val cols = heightMap.head.length



    if (rows < 3 || cols < 3) {

      return 0

    }



    val visited = Array.fill(rows, cols)(false)

    val heap = mutable.PriorityQueue.empty[(Int, Int, Int)](Ordering.by(-_._1))



    for (row <- 0 until rows; col <- 0 until cols) {

      if (row == 0 || row == rows - 1 || col == 0 || col == cols - 1) {

        heap.enqueue((heightMap(row)(col), row, col))

        visited(row)(col) = true

      }

    }



    var trapped = 0

    val directions = Seq((1, 0), (-1, 0), (0, 1), (0, -1))



    while (heap.nonEmpty) {

      val (height, row, col) = heap.dequeue()



      for ((dr, dc) <- directions) {

        val nextRow = row + dr

        val nextCol = col + dc



        if (nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols

            || visited(nextRow)(nextCol)) {

          // skip

        } else {

          visited(nextRow)(nextCol) = true

          val nextHeight = heightMap(nextRow)(nextCol)

          trapped += math.max(0, height - nextHeight)

          heap.enqueue((math.max(height, nextHeight), nextRow, nextCol))

        }

      }

    }



    trapped

  }

}
