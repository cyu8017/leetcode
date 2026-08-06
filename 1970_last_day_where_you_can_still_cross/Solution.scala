// LeetCode 1970 - Last Day Where You Can Still Cross
// https://leetcode.com/problems/last-day-where-you-can-still-cross/

object Solution {
  def latestDayToCross(row: Int, col: Int, cells: Array[Array[Int]]): Int = {
    def can(day: Int): Boolean = {
      val blocked = scala.collection.mutable.Set.empty[(Int, Int)]
      for (i <- 0 until day) blocked += ((cells(i)(0) - 1, cells(i)(1) - 1))
      val stack = scala.collection.mutable.ArrayBuffer.empty[(Int, Int)]
      val seen = scala.collection.mutable.Set.empty[(Int, Int)]
      for (c <- 0 until col if !blocked.contains((0, c))) {
        stack += ((0, c))
        seen += ((0, c))
      }
      while (stack.nonEmpty) {
        val (r, c) = stack.remove(stack.length - 1)
        if (r == row - 1) return true
        for ((nr, nc) <- Seq((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))) {
          if (nr >= 0 && nr < row && nc >= 0 && nc < col &&
              !blocked.contains((nr, nc)) && !seen.contains((nr, nc))) {
            seen += ((nr, nc))
            stack += ((nr, nc))
          }
        }
      }
      false
    }
    var lo = 1
    var hi = cells.length
    var ans = 0
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      if (can(mid)) { ans = mid; lo = mid + 1 }
      else hi = mid - 1
    }
    ans
  }
}
