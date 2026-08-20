// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

object Solution {
  def shiftGrid(grid: Array[Array[Int]], k: Int): List[List[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val flat = grid.flatten
    val kk = k % flat.length
    val shifted = if (kk == 0) flat else flat.takeRight(kk) ++ flat.dropRight(kk)
    (0 until m).map(i => shifted.slice(i * n, (i + 1) * n).toList).toList
  }
}
