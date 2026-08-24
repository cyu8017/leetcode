// LeetCode 0750 - Number Of Corner Rectangles
// https://leetcode.com/problems/number-of-corner-rectangles/

object Solution {
  def countCornerRectangles(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var ans = 0
    var i = 0
    while (i < m) {
      var j = i + 1
      while (j < m) {
        var count = 0
        var c = 0
        while (c < n) {
          if (grid(i)(c) == 1 && grid(j)(c) == 1) count += 1
          c += 1
        }
        ans += count * (count - 1) / 2
        j += 1
      }
      i += 1
    }
    ans
  }
}
