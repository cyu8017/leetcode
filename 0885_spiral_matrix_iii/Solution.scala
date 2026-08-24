// LeetCode 0885 - Spiral Matrix III
// https://leetcode.com/problems/spiral-matrix-iii/

object Solution {
  def spiralMatrixIII(rows: Int, cols: Int, rStart: Int, cStart: Int): Array[Array[Int]] = {
    val ans = scala.collection.mutable.ArrayBuffer[Array[Int]]()
    ans += Array(rStart, cStart)
    if (rows * cols == 1) return ans.toArray
    var r = rStart
    var c = cStart
    val dirs = Array(Array(0, 1), Array(1, 0), Array(0, -1), Array(-1, 0))
    var steps = 1
    while (ans.length < rows * cols) {
      var d = 0
      while (d < 4) {
        val dr = dirs(d)(0)
        val dc = dirs(d)(1)
        var i = 0
        while (i < steps) {
          r += dr
          c += dc
          if (r >= 0 && r < rows && c >= 0 && c < cols) {
            ans += Array(r, c)
            if (ans.length == rows * cols) return ans.toArray
          }
          i += 1
        }
        if (d % 2 == 1) steps += 1
        d += 1
      }
    }
    ans.toArray
  }
}
