// LeetCode 1034 - Coloring A Border
// https://leetcode.com/problems/coloring-a-border/

object Solution {
  def colorBorder(grid: Array[Array[Int]], row: Int, col: Int, color: Int): Array[Array[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val original = grid(row)(col)
    val component = scala.collection.mutable.Set.empty[(Int, Int)]
    val stack = scala.collection.mutable.ArrayBuffer((row, col))
    component.add((row, col))
    while (stack.nonEmpty) {
      val (r, c) = stack.remove(stack.length - 1)
      for ((nr, nc) <- Seq((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))) {
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) == original && !component.contains((nr, nc))) {
          component.add((nr, nc))
          stack += ((nr, nc))
        }
      }
    }
    val border = scala.collection.mutable.ArrayBuffer.empty[(Int, Int)]
    for ((r, c) <- component) {
      var isBorder = false
      for ((nr, nc) <- Seq((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)) if !isBorder) {
        if (nr < 0 || nr >= m || nc < 0 || nc >= n || !component.contains((nr, nc))) {
          isBorder = true
        }
      }
      if (isBorder) border += ((r, c))
    }
    for ((r, c) <- border) grid(r)(c) = color
    grid
  }
}
