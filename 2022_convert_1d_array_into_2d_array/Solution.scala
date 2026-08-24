// LeetCode 2022 - Convert 1D Array Into 2D Array
// https://leetcode.com/problems/convert-1d-array-into-2d-array/

object Solution {
  def construct2DArray(original: Array[Int], m: Int, n: Int): Array[Array[Int]] = {
    if (original.length != m * n) return Array.empty[Array[Int]]
    val ans = Array.ofDim[Int](m, n)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        ans(i)(j) = original(i * n + j)
        j += 1
      }
      i += 1
    }
    ans
  }
}
