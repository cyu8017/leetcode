// LeetCode 0279 - Perfect Squares
// https://leetcode.com/problems/perfect-squares/

import scala.collection.mutable

object Solution {
  def numSquares(n: Int): Int = {
    val squares = Iterator.from(1).takeWhile(v => v * v <= n).map(v => v * v).toList
    val queue = mutable.Queue((n, 0))
    val visited = mutable.Set(n)

    while (queue.nonEmpty) {
      val (remain, steps) = queue.dequeue()
      if (remain == 0) {
        return steps
      }
      for (square <- squares) {
        val next = remain - square
        if (next >= 0 && !visited.contains(next)) {
          visited.add(next)
          queue.enqueue((next, steps + 1))
        }
      }
    }
    0
  }
}
