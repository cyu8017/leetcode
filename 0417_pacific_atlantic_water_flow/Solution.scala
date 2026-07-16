// LeetCode 0417 - Pacific Atlantic Water Flow

// https://leetcode.com/problems/pacific-atlantic-water-flow/



import scala.collection.mutable



object Solution {

  def pacificAtlantic(heights: Array[Array[Int]]): List[List[Int]] = {

    if (heights.isEmpty || heights(0).isEmpty) {

      return List.empty

    }



    val rows = heights.length

    val cols = heights(0).length

    val pacific = mutable.Set.empty[Long]

    val atlantic = mutable.Set.empty[Long]



    for (row <- 0 until rows) {

      dfs(row, 0, pacific, heights(row)(0), heights, rows, cols)

      dfs(row, cols - 1, atlantic, heights(row)(cols - 1), heights, rows, cols)

    }



    for (col <- 0 until cols) {

      dfs(0, col, pacific, heights(0)(col), heights, rows, cols)

      dfs(rows - 1, col, atlantic, heights(rows - 1)(col), heights, rows, cols)

    }



    pacific.intersect(atlantic).map { key =>

      List((key / cols).toInt, (key % cols).toInt)

    }.toList

  }



  private def dfs(

      row: Int,

      col: Int,

      visited: mutable.Set[Long],

      previous: Int,

      heights: Array[Array[Int]],

      rows: Int,

      cols: Int,

  ): Unit = {

    val key = row.toLong * cols + col



    if (visited.contains(key) || row < 0 || row >= rows || col < 0 || col >= cols) {

      return

    }



    if (heights(row)(col) < previous) {

      return

    }



    visited.add(key)

    val height = heights(row)(col)



    dfs(row + 1, col, visited, height, heights, rows, cols)

    dfs(row - 1, col, visited, height, heights, rows, cols)

    dfs(row, col + 1, visited, height, heights, rows, cols)

    dfs(row, col - 1, visited, height, heights, rows, cols)

  }

}
