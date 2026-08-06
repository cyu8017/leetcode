// LeetCode 1572 - Matrix Diagonal Sum
// https://leetcode.com/problems/matrix-diagonal-sum/

object Solution {
  def diagonalSum(mat: Array[Array[Int]]): Int = {
    val n = mat.length
    var sum = 0
    for (i <- 0 until n) sum += mat(i)(i) + mat(i)(n - 1 - i)
    if (n % 2 == 1) sum -= mat(n / 2)(n / 2)
    sum
  }
}
