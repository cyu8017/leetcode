// LeetCode 1591 - Strange Printer II
// https://leetcode.com/problems/strange-printer-ii/

object Solution {
  def isPrintable(targetGrid: Array[Array[Int]]): Boolean = {
    val colors = targetGrid.flatten.toSet
    val bounds = colors.map(c => c -> Array(Int.MaxValue, Int.MaxValue, -1, -1)).toMap
    for (r <- targetGrid.indices; c <- targetGrid(0).indices) {
      val color = targetGrid(r)(c)
      val b = bounds(color)
      b(0) = math.min(b(0), r)
      b(1) = math.min(b(1), c)
      b(2) = math.max(b(2), r)
      b(3) = math.max(b(3), c)
    }
    val graph = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.Set[Int]]
    val indegree = colors.map(_ -> 0).to(scala.collection.mutable.Map)
    for (c <- colors) {
      graph.getOrElseUpdate(c, scala.collection.mutable.Set.empty)
      val Array(r1, c1, r2, c2) = bounds(c)
      for (r <- r1 to r2; col <- c1 to c2) {
        val other = targetGrid(r)(col)
        if (other != c && !graph(c).contains(other)) {
          graph(c) += other
          indegree(other) = indegree.getOrElse(other, 0) + 1
        }
      }
    }
    val queue = scala.collection.mutable.Queue.from(colors.filter(indegree(_) == 0))
    var seen = 0
    while (queue.nonEmpty) {
      val c = queue.dequeue()
      seen += 1
      for (nxt <- graph.getOrElse(c, Set.empty)) {
        indegree(nxt) -= 1
        if (indegree(nxt) == 0) queue.enqueue(nxt)
      }
    }
    seen == colors.size
  }
}
