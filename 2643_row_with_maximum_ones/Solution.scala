// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

object Solution {
  def rowAndMaximumOnes(mat: Array[Array[Int]]): Array[Int] = {
    var bestRow = 0
    var bestCnt = -1
    var i = 0
    while (i < mat.length) {
      var cnt = 0
      var j = 0
      while (j < mat(i).length) {
        cnt += mat(i)(j)
        j += 1
      }
      if (cnt > bestCnt) {
        bestCnt = cnt
        bestRow = i
      }
      i += 1
    }
    Array(bestRow, bestCnt)
  }
}
