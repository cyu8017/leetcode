// LeetCode 1277 - Count Square Submatrices with All Ones
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

object Solution {
  def countSquares(matrix: Array[Array[Int]]): Int = {
    var answer = 0
    for (r <- matrix.indices; c <- matrix(0).indices) {
      if (matrix(r)(c) > 0 && r > 0 && c > 0) {
        matrix(r)(c) += math.min(matrix(r - 1)(c), math.min(matrix(r)(c - 1), matrix(r - 1)(c - 1)))
      }
      answer += matrix(r)(c)
    }
    answer
  }
}
