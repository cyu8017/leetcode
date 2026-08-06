import scala.collection.mutable

object Solution {
  def minCost(grid: Array[Array[Int]]): Int = {
    val rows = grid.length; val cols = grid.head.length; val dist = Array.fill(rows, cols)(Int.MaxValue)
    val deque = mutable.ArrayDeque((0, 0)); dist(0)(0) = 0
    val directions = Array((0, 1), (0, -1), (1, 0), (-1, 0))
    while (deque.nonEmpty) {
      val (r, c) = deque.removeHead()
      directions.indices.foreach(k => { val (dr, dc) = directions(k); val nr = r + dr; val nc = c + dc
        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) { val cost = if (grid(r)(c) == k + 1) 0 else 1; val next = dist(r)(c) + cost
          if (next < dist(nr)(nc)) { dist(nr)(nc) = next; if (cost == 0) deque.prepend((nr, nc)) else deque.append((nr, nc)) }
        }
      })
    }
    dist(rows - 1)(cols - 1)
  }
}
