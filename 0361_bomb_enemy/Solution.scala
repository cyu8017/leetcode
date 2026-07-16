// LeetCode 0361 - Bomb Enemy

// https://leetcode.com/problems/bomb-enemy/



object Solution {

  def maxKilledEnemies(grid: Array[Array[Char]]): Int = {

    if (grid.isEmpty || grid(0).isEmpty) return 0



    val rows = grid.length

    val cols = grid(0).length

    val rowHits = Array.ofDim[Int](rows, cols)

    val colHits = Array.ofDim[Int](rows, cols)



    for (row <- 0 until rows) {

      var count = 0

      for (col <- 0 until cols) {

        grid(row)(col) match {

          case 'W' => count = 0

          case 'E' => count += 1

          case _   => rowHits(row)(col) = count

        }

      }

      count = 0

      for (col <- cols - 1 to 0 by -1) {

        grid(row)(col) match {

          case 'W' => count = 0

          case 'E' => count += 1

          case _   => rowHits(row)(col) += count

        }

      }

    }



    for (col <- 0 until cols) {

      var count = 0

      for (row <- 0 until rows) {

        grid(row)(col) match {

          case 'W' => count = 0

          case 'E' => count += 1

          case _   => colHits(row)(col) = count

        }

      }

      count = 0

      for (row <- rows - 1 to 0 by -1) {

        grid(row)(col) match {

          case 'W' => count = 0

          case 'E' => count += 1

          case _   => colHits(row)(col) += count

        }

      }

    }



    var result = 0

    for (row <- 0 until rows; col <- 0 until cols) {

      result = math.max(result, rowHits(row)(col) + colHits(row)(col))

    }

    result

  }

}
