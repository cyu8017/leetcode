// LeetCode 0329 - Longest Increasing Path in a Matrix

// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/



object Solution {

  private var matrix: Array[Array[Int]] = _

  private var memo: Array[Array[Int]] = _



  private val directions = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))



  def longestIncreasingPath(matrix: Array[Array[Int]]): Int = {

    if (matrix.isEmpty || matrix(0).isEmpty) {

      return 0

    }

    this.matrix = matrix

    memo = Array.ofDim[Int](matrix.length, matrix(0).length)

    var best = 0

    for (row <- matrix.indices) {

      for (col <- matrix(0).indices) {

        best = math.max(best, dfs(row, col))

      }

    }

    best

  }



  private def dfs(row: Int, col: Int): Int = {

    if (memo(row)(col) != 0) {

      return memo(row)(col)

    }

    var best = 1

    for (Array(dr, dc) <- directions) {

      val nextRow = row + dr

      val nextCol = col + dc

      if (nextRow >= 0 && nextRow < matrix.length && nextCol >= 0 && nextCol < matrix(0).length

        && matrix(nextRow)(nextCol) > matrix(row)(col)) {

        best = math.max(best, 1 + dfs(nextRow, nextCol))

      }

    }

    memo(row)(col) = best

    best

  }

}

