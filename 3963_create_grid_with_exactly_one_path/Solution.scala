// LeetCode 3963 - Create Grid With Exactly One Path
// https://leetcode.com/problems/create-grid-with-exactly-one-path/

object Solution {
  def createGrid(m: Int, n: Int): Array[String] = {
    val g = new Array[String](m)
    var i = 0
    while (i < m) {
      val row = Array.fill(n)('#')
      if (i == 0) {
        var j = 0
        while (j < n) {
          row(j) = '.'
          j += 1
        }
      }
      row(n - 1) = '.'
      g(i) = new String(row)
      i += 1
    }
    g
  }
}
