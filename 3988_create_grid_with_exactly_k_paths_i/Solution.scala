// LeetCode 3988 - Create Grid With Exactly K Paths I
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

object Solution {
  def createGrid(m: Int, n: Int, k: Int): Array[String] = {
    val cands = scala.collection.mutable.ArrayBuffer.empty[Array[String]]
    if (k == 1) cands += Array(".")
    else if (k == 2) cands += Array("..", "..")
    else if (k == 3) {
      cands += Array("..", "..", "..")
      cands += Array("...", "...")
    } else if (k == 4) {
      cands += Array("..", "..", "..", "..")
      cands += Array("....", "....")
      cands += Array("..#", "...", "#..")
    }
    for (pat <- cands) {
      val pr = pat.length
      val pc = pat(0).length
      if (pr <= m && pc <= n) {
        val result = new Array[String](m)
        var i = 0
        while (i < m) {
          val row = Array.fill(n)('#')
          result(i) = new String(row)
          i += 1
        }
        i = 0
        while (i < pr) {
          val row = result(i).toCharArray
          var j = 0
          while (j < pc) {
            row(j) = pat(i).charAt(j)
            j += 1
          }
          result(i) = new String(row)
          i += 1
        }
        i = pr
        while (i < m) {
          val row = result(i).toCharArray
          row(pc - 1) = '.'
          result(i) = new String(row)
          i += 1
        }
        var j = pc
        while (j < n) {
          val row = result(m - 1).toCharArray
          row(j) = '.'
          result(m - 1) = new String(row)
          j += 1
        }
        return result
      }
    }
    Array.empty[String]
  }
}
