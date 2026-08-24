// LeetCode 0778 - Swim in Rising Water
// https://leetcode.com/problems/swim-in-rising-water/

object Solution {
  def swimInWater(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val heap = scala.collection.mutable.PriorityQueue.empty[(Int, Int, Int)](Ordering.by[(Int, Int, Int), Int](_._1).reverse)
    val seen = Array.ofDim[Boolean](n, n)
    heap.enqueue((grid(0)(0), 0, 0))
    seen(0)(0) = true
    val dirs = Array(Array(-1, 0), Array(1, 0), Array(0, -1), Array(0, 1))
    while (heap.nonEmpty) {
      val (time, r, c) = heap.dequeue()
      if (r == n - 1 && c == n - 1) return time
      for (d <- dirs) {
        val nr = r + d(0)
        val nc = c + d(1)
        if (nr >= 0 && nr < n && nc >= 0 && nc < n && !seen(nr)(nc)) {
          seen(nr)(nc) = true
          val nt = math.max(time, grid(nr)(nc))
          heap.enqueue((nt, nr, nc))
        }
      }
    }
    -1
  }
}
