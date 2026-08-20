// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

object Solution {
  def minPushBox(grid: Array[Array[Char]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var box = (0, 0)
    var player = (0, 0)
    var target = (0, 0)
    for (r <- 0 until m; c <- 0 until n) {
      if (grid(r)(c) == 'B') box = (r, c)
      else if (grid(r)(c) == 'S') player = (r, c)
      else if (grid(r)(c) == 'T') target = (r, c)
    }
    def reachable(start: (Int, Int), blocked: (Int, Int)): Set[(Int, Int)] = {
      val seen = scala.collection.mutable.Set(start)
      val stack = scala.collection.mutable.Stack(start)
      while (stack.nonEmpty) {
        val (r, c) = stack.pop()
        for ((dr, dc) <- Seq((1, 0), (-1, 0), (0, 1), (0, -1))) {
          val nxt = (r + dr, c + dc)
          if (nxt._1 >= 0 && nxt._1 < m && nxt._2 >= 0 && nxt._2 < n &&
              grid(nxt._1)(nxt._2) != '#' && nxt != blocked && !seen.contains(nxt)) {
            seen += nxt
            stack.push(nxt)
          }
        }
      }
      seen.toSet
    }
    val q = scala.collection.mutable.Queue((box, player, 0))
    val seen = scala.collection.mutable.Set((box, player))
    while (q.nonEmpty) {
      val (b, p, pushes) = q.dequeue()
      if (b == target) return pushes
      val canReach = reachable(p, b)
      for ((dr, dc) <- Seq((1, 0), (-1, 0), (0, 1), (0, -1))) {
        val stand = (b._1 - dr, b._2 - dc)
        val nb = (b._1 + dr, b._2 + dc)
        if (canReach.contains(stand) && nb._1 >= 0 && nb._1 < m && nb._2 >= 0 && nb._2 < n &&
            grid(nb._1)(nb._2) != '#') {
          val state = (nb, b)
          if (!seen.contains(state)) {
            seen += state
            q.enqueue((nb, b, pushes + 1))
          }
        }
      }
    }
    -1
  }
}
