// LeetCode 1568 - Minimum Number of Days to Disconnect Island
// https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

object Solution {
  def minDays(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    def islands(): Int = {
      val seen = scala.collection.mutable.Set.empty[(Int, Int)]
      var count = 0
      for (r <- 0 until m; c <- 0 until n if grid(r)(c) == 1 && !seen.contains((r, c))) {
        count += 1
        val stack = scala.collection.mutable.Stack((r, c))
        seen += ((r, c))
        while (stack.nonEmpty) {
          val (x, y) = stack.pop()
          for ((dx, dy) <- Seq((1, 0), (-1, 0), (0, 1), (0, -1))) {
            val nx = x + dx
            val ny = y + dy
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid(nx)(ny) == 1 && !seen.contains((nx, ny))) {
              seen += ((nx, ny))
              stack.push((nx, ny))
            }
          }
        }
      }
      count
    }
    if (islands() != 1) return 0
    for (r <- 0 until m; c <- 0 until n if grid(r)(c) == 1) {
      grid(r)(c) = 0
      if (islands() != 1) {
        grid(r)(c) = 1
        return 1
      }
      grid(r)(c) = 1
    }
    2
  }
}
