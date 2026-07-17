// LeetCode 1738 - Find Kth Largest XOR Coordinate Value
// https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

object Solution {
  def kthLargestValue(matrix: Array[Array[Int]], k: Int): Int = {
    val rows = matrix.length
    val cols = matrix(0).length
    val pref = Array.ofDim[Int](rows + 1, cols + 1)
    val values = new Array[Int](rows * cols)
    var index = 0
    for (r <- 1 to rows; c <- 1 to cols) {
      pref(r)(c) = pref(r - 1)(c) ^ pref(r)(c - 1) ^ pref(r - 1)(c - 1) ^ matrix(r - 1)(c - 1)
      values(index) = pref(r)(c)
      index += 1
    }
    java.util.Arrays.sort(values)
    values(values.length - k)
  }
}
