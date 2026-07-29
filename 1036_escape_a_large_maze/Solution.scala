// LeetCode 1036 - Escape a Large Maze
// https://leetcode.com/problems/escape-a-large-maze/

import scala.collection.mutable

object Solution {
  def isEscapePossible(blocked: Array[Array[Int]], source: Array[Int], target: Array[Int]): Boolean = {
    val blockedSet = blocked.map(b => (b(0), b(1))).toSet
    val limit = blocked.length.toLong * (blocked.length - 1) / 2

    def bfs(start: Array[Int], goal: Array[Int]): Boolean = {
      val queue = mutable.Queue((start(0), start(1)))
      val seen = mutable.Set((start(0), start(1)))
      while (queue.nonEmpty) {
        if (seen.size > limit) return true
        val (r, c) = queue.dequeue()
        if (r == goal(0) && c == goal(1)) return true
        for ((nr, nc) <- Seq((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))) {
          if (nr >= 0 && nr < 1000000 && nc >= 0 && nc < 1000000 &&
              !blockedSet.contains((nr, nc)) && !seen.contains((nr, nc))) {
            seen.add((nr, nc))
            queue.enqueue((nr, nc))
          }
        }
      }
      false
    }

    bfs(source, target) && bfs(target, source)
  }
}
