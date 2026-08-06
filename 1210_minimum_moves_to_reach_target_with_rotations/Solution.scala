// LeetCode 1210 - Minimum Moves to Reach Target with Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

object Solution {
  def minimumMoves(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val start = (0, 0, 0)
    val target = (n - 1, n - 2, 0)
    val q = scala.collection.mutable.Queue((start, 0))
    val seen = scala.collection.mutable.Set(start)
    while (q.nonEmpty) {
      val ((r, c, orient), moves) = q.dequeue()
      if ((r, c, orient) == target) return moves
      val nxt = scala.collection.mutable.ListBuffer.empty[(Int, Int, Int)]
      if (orient == 0) {
        if (c + 2 < n && grid(r)(c + 2) == 0) nxt += ((r, c + 1, 0))
        if (r + 1 < n && grid(r + 1)(c) == 0 && grid(r + 1)(c + 1) == 0) {
          nxt += ((r + 1, c, 0))
          nxt += ((r, c, 1))
        }
      } else {
        if (r + 2 < n && grid(r + 2)(c) == 0) nxt += ((r + 1, c, 1))
        if (c + 1 < n && grid(r)(c + 1) == 0 && grid(r + 1)(c + 1) == 0) {
          nxt += ((r, c + 1, 1))
          nxt += ((r, c, 0))
        }
      }
      for (state <- nxt if !seen.contains(state)) {
        seen += state
        q.enqueue((state, moves + 1))
      }
    }
    -1
  }
}
