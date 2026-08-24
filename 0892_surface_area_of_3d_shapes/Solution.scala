// LeetCode 0892 - Surface Area of 3D Shapes
// https://leetcode.com/problems/surface-area-of-3d-shapes/

object Solution {
  def surfaceArea(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    var area = 0
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) != 0) {
          area += grid(i)(j) * 4 + 2
          if (i > 0) area -= math.min(grid(i)(j), grid(i - 1)(j)) * 2
          if (j > 0) area -= math.min(grid(i)(j), grid(i)(j - 1)) * 2
        }
        j += 1
      }
      i += 1
    }
    area
  }
}
