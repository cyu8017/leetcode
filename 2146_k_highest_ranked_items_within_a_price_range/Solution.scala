// LeetCode 2146 - K Highest Ranked Items Within a Price Range
// https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

object Solution {
  def highestRankedKItems(grid: Array[Array[Int]], pricing: Array[Int], start: Array[Int], k: Int): List[List[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val low = pricing(0)
    val high = pricing(1)
    val vis = Array.fill(m, n)(false)
    val q = scala.collection.mutable.Queue[(Int, Int, Int)]()
    q.enqueue((start(0), start(1), 0))
    vis(start(0))(start(1)) = true
    val cands = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    while (q.nonEmpty) {
      val (r, c, d) = q.dequeue()
      if (grid(r)(c) >= low && grid(r)(c) <= high) cands += Array(d, grid(r)(c), r, c)
      dirs.foreach { case (dr, dc) =>
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !vis(nr)(nc) && grid(nr)(nc) != 0) {
          vis(nr)(nc) = true
          q.enqueue((nr, nc, d + 1))
        }
      }
    }
    val sorted = cands.sortBy(a => (a(0), a(1), a(2), a(3)))
    val take = math.min(k, sorted.length)
    (0 until take).map(i => List(sorted(i)(2), sorted(i)(3))).toList
  }
}
