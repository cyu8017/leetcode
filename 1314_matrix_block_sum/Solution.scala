// LeetCode 1314 - Matrix Block Sum
// https://leetcode.com/problems/matrix-block-sum/

object Solution {
  def matrixBlockSum(mat: Array[Array[Int]], k: Int): Array[Array[Int]] = {
    val m = mat.length
    val n = mat(0).length
    val prefix = Array.ofDim[Int](m + 1, n + 1)
    for (r <- 0 until m; c <- 0 until n) {
      prefix(r + 1)(c + 1) = mat(r)(c) + prefix(r)(c + 1) + prefix(r + 1)(c) - prefix(r)(c)
    }
    val answer = Array.ofDim[Int](m, n)
    for (r <- 0 until m; c <- 0 until n) {
      val r1 = math.max(0, r - k)
      val c1 = math.max(0, c - k)
      val r2 = math.min(m, r + k + 1)
      val c2 = math.min(n, c + k + 1)
      answer(r)(c) = prefix(r2)(c2) - prefix(r1)(c2) - prefix(r2)(c1) + prefix(r1)(c1)
    }
    answer
  }
}
