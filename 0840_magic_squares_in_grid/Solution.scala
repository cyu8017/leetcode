// LeetCode 0840 - Magic Squares In Grid
// https://leetcode.com/problems/magic-squares-in-grid/

object Solution {
  def numMagicSquaresInside(grid: Array[Array[Int]]): Int = {
    val rows = grid.length
    val cols = grid(0).length
    if (rows < 3 || cols < 3) return 0
    def magic(r: Int, c: Int): Boolean = {
      val vals = Array.ofDim[Int](9)
      var k = 0
      var i = 0
      while (i < 3) {
        var j = 0
        while (j < 3) {
          vals(k) = grid(r + i)(c + j)
          k += 1
          j += 1
        }
        i += 1
      }
      scala.util.Sorting.quickSort(vals)
      i = 0
      while (i < 9) {
        if (vals(i) != i + 1) return false
        i += 1
      }
      grid(r)(c) + grid(r)(c + 1) + grid(r)(c + 2) == 15 &&
        grid(r + 1)(c) + grid(r + 1)(c + 1) + grid(r + 1)(c + 2) == 15 &&
        grid(r + 2)(c) + grid(r + 2)(c + 1) + grid(r + 2)(c + 2) == 15 &&
        grid(r)(c) + grid(r + 1)(c) + grid(r + 2)(c) == 15 &&
        grid(r)(c + 1) + grid(r + 1)(c + 1) + grid(r + 2)(c + 1) == 15 &&
        grid(r)(c + 2) + grid(r + 1)(c + 2) + grid(r + 2)(c + 2) == 15 &&
        grid(r)(c) + grid(r + 1)(c + 1) + grid(r + 2)(c + 2) == 15 &&
        grid(r)(c + 2) + grid(r + 1)(c + 1) + grid(r + 2)(c) == 15
    }
    var ans = 0
    var i = 0
    while (i < rows - 2) {
      var j = 0
      while (j < cols - 2) {
        if (magic(i, j)) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
