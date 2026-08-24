// LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
// https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

object Solution {
  def findPattern(board: Array[Array[Int]], pattern: Array[String]): Array[Int] = {
    val m = board.length
    val n = board(0).length
    val r = pattern.length
    val c = pattern(0).length
    var i = 0
    while (i < m - r + 1) {
      var j = 0
      while (j < n - c + 1) {
        if (check(board, pattern, i, j, r, c)) return Array(i, j)
        j += 1
      }
      i += 1
    }
    Array(-1, -1)
  }

  private def check(board: Array[Array[Int]], pattern: Array[String], i: Int, j: Int, r: Int, c: Int): Boolean = {
    val d1 = new Array[Int](26)
    val d2 = new Array[Int](10)
    var a = 0
    while (a < r) {
      var b = 0
      while (b < c) {
        val x = i + a
        val y = j + b
        val ch = pattern(a).charAt(b)
        if (ch >= '0' && ch <= '9') {
          if (ch - '0' != board(x)(y)) return false
        } else {
          val v = ch - 'a'
          if (d1(v) > 0 && d1(v) - 1 != board(x)(y)) return false
          if (d2(board(x)(y)) > 0 && d2(board(x)(y)) - 1 != v) return false
          d1(v) = board(x)(y) + 1
          d2(board(x)(y)) = v + 1
        }
        b += 1
      }
      a += 1
    }
    true
  }
}
