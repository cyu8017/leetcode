// LeetCode 0311 - Sparse Matrix Multiplication

// https://leetcode.com/problems/sparse-matrix-multiplication/



object Solution {

  def multiply(mat1: Array[Array[Int]], mat2: Array[Array[Int]]): Array[Array[Int]] = {

    val rows = mat1.length

    val inner = mat1(0).length

    val cols = mat2(0).length

    val result = Array.fill(rows, cols)(0)

    for (row <- 0 until rows) {

      for (index <- 0 until inner if mat1(row)(index) != 0) {

        for (col <- 0 until cols if mat2(index)(col) != 0) {

          result(row)(col) += mat1(row)(index) * mat2(index)(col)

        }

      }

    }

    result

  }

}

