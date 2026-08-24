// LeetCode 0847 - Shortest Path Visiting All Nodes
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/

object Solution {
  def shortestPathLength(graph: Array[Array[Int]]): Int = {
    val n = graph.length
    val target = (1 << n) - 1
    val queue = scala.collection.mutable.Queue.empty[(Int, Int, Int)]
    val seen = scala.collection.mutable.Set.empty[Long]
    var i = 0
    while (i < n) {
      queue.enqueue((i, 1 << i, 0))
      seen += ((i.toLong << 20) | (1 << i))
      i += 1
    }
    while (queue.nonEmpty) {
      val (node, mask, dist) = queue.dequeue()
      if (mask == target) return dist
      graph(node).foreach { nxt =>
        val nmask = mask | (1 << nxt)
        val state = (nxt.toLong << 20) | nmask
        if (seen.add(state)) queue.enqueue((nxt, nmask, dist + 1))
      }
    }
    -1
  }
}
