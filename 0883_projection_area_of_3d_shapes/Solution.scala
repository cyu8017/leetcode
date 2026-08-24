// LeetCode 0883 - Projection Area of 3D Shapes
// https://leetcode.com/problems/projection-area-of-3d-shapes/

object Solution {
  def projectionArea(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    var top = 0
    var front = 0
    var side = 0
    var i = 0
    while (i < n) {
      var rowMax = 0
      var colMax = 0
      var j = 0
      while (j < n) {
        if (grid(i)(j) != 0) top += 1
        rowMax = math.max(rowMax, grid(i)(j))
        colMax = math.max(colMax, grid(j)(i))
        j += 1
      }
      front += rowMax
      side += colMax
      i += 1
    }
    top + front + side
  }
}
