// LeetCode 3195 - Find the Minimum Area to Cover All Ones I
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

object Solution {
  def minimumArea(grid: Array[Array[Int]]): Int = {
    var x1 = grid.length
    var y1 = grid(0).length
    var x2 = 0
    var y2 = 0
    var i = 0
    while (i < grid.length) {
      var j = 0
      while (j < grid(0).length) {
        if (grid(i)(j) == 1) {
          x1 = math.min(x1, i); y1 = math.min(y1, j)
          x2 = math.max(x2, i); y2 = math.max(y2, j)
        }
        j += 1
      }
      i += 1
    }
    (x2 - x1 + 1) * (y2 - y1 + 1)
  }
}
