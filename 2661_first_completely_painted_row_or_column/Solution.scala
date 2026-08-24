// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

object Solution {
  def firstCompleteIndex(arr: Array[Int], mat: Array[Array[Int]]): Int = {
    val m = mat.length
    val n = mat(0).length
    val posR = new Array[Int](m * n + 1)
    val posC = new Array[Int](m * n + 1)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        posR(mat(i)(j)) = i
        posC(mat(i)(j)) = j
        j += 1
      }
      i += 1
    }
    val rowCnt = new Array[Int](m)
    val colCnt = new Array[Int](n)
    i = 0
    while (i < arr.length) {
      val r = posR(arr(i))
      val c = posC(arr(i))
      rowCnt(r) += 1
      colCnt(c) += 1
      if (rowCnt(r) == n || colCnt(c) == m) return i
      i += 1
    }
    -1
  }
}
