// LeetCode 3127 - Make a Square with the Same Color
// https://leetcode.com/problems/make-a-square-with-the-same-color/

object Solution {
  def canMakeSquare(grid: Array[Array[Char]]): Boolean = {
    val dirs = Array(0, 0, 1, 1, 0)
    var i = 0
    while (i < 2) {
      var j = 0
      while (j < 2) {
        var cnt1 = 0
        var cnt2 = 0
        var k = 0
        while (k < 4) {
          val x = i + dirs(k)
          val y = j + dirs(k + 1)
          if (grid(x)(y) == 'W') cnt1 += 1
          else cnt2 += 1
          k += 1
        }
        if (cnt1 != cnt2) return true
        j += 1
      }
      i += 1
    }
    false
  }
}
