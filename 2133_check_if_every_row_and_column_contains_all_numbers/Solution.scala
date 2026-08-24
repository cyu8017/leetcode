// LeetCode 2133 - Check if Every Row and Column Contains All Numbers
// https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

object Solution {
  def checkValid(matrix: Array[Array[Int]]): Boolean = {
    val n = matrix.length
    var i = 0
    while (i < n) {
      val row = Array.fill(n + 1)(false)
      val col = Array.fill(n + 1)(false)
      var j = 0
      while (j < n) {
        if (row(matrix(i)(j)) || col(matrix(j)(i))) return false
        row(matrix(i)(j)) = true
        col(matrix(j)(i)) = true
        j += 1
      }
      i += 1
    }
    true
  }
}
