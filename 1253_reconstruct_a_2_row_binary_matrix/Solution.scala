// LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

object Solution {
  def reconstructMatrix(upper: Int, lower: Int, colsum: Array[Int]): List[List[Int]] = {
    var u = upper
    var l = lower
    val top = Array.fill(colsum.length)(0)
    val bottom = Array.fill(colsum.length)(0)
    for (i <- colsum.indices if colsum(i) == 2) {
      top(i) = 1
      bottom(i) = 1
      u -= 1
      l -= 1
    }
    if (u < 0 || l < 0) return List.empty
    for (i <- colsum.indices if colsum(i) == 1) {
      if (u > 0) { top(i) = 1; u -= 1 }
      else if (l > 0) { bottom(i) = 1; l -= 1 }
      else return List.empty
    }
    if (u == 0 && l == 0) List(top.toList, bottom.toList) else List.empty
  }
}
